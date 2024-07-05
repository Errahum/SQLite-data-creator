import csv
import json
import pandas as pd
from .db_manager import insert_data, create_table


def load_parquet(file_path):
    """Charge les données d'un fichier Parquet"""
    return pd.read_parquet(file_path)


def load_json(file_path):
    """Charge les données d'un fichier JSON"""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def load_data_to_db_all_tables(db_conn, file_path, file_type):
    """Charge toutes les tables disponibles à partir d'un fichier Parquet, JSON ou CSV dans des tables SQLite"""
    main_table_name = file_path.split('/')[-1].split('.')[0].replace(" ", "_")

    if file_type.lower() == 'parquet':
        try:
            data = pd.read_parquet(file_path)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier Parquet : {e}")
            return

        main_table_data = {}
        for column_name in data.columns:
            table_name = column_name.replace(" ", "_")
            table_data = data[[column_name]].dropna().reset_index(drop=True)
            main_table_data[table_name] = [str(x) for x in table_data[column_name]]

    elif file_type.lower() == 'csv':
        main_table_data = {}
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Récupère les en-têtes
                num_columns = len(headers)

                for column_name in headers:
                    table_name = column_name.replace(" ", "_")
                    csvfile.seek(0)  # Réinitialiser la position du fichier
                    next(reader)  # Skip headers again
                    table_data = [row[headers.index(column_name)] for row in reader if row and len(row) >= num_columns]
                    main_table_data[table_name] = [str(x) for x in table_data]

        except Exception as e:
            print(f"Erreur lors de la lecture du fichier CSV : {e}")
            return

    elif file_type.lower() == 'json':
        try:
            data = load_json(file_path)
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")
            return

        main_table_data = {}
        for table_name, table_data in data.items():
            if isinstance(table_data, list) and all(isinstance(row, str) for row in table_data):
                table_data = [{"value": row} for row in table_data]
            if all(isinstance(row, dict) for row in table_data):
                main_table_data[table_name] = table_data

    else:
        print("Type de fichier non supporté.")
        return

    # Création de la table principale pour contenir toutes les autres tables
    if main_table_data:
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {main_table_name} (table_name TEXT, data TEXT);"
        create_table(db_conn, create_table_sql)

        main_records = [{"table_name": k, "data": json.dumps(v)} for k, v in main_table_data.items()]
        insert_data(db_conn, main_table_name, [tuple(record.values()) for record in main_records])

        # Création de tables séparées pour chaque sous-table
        for sub_table_name, sub_table_data in main_table_data.items():
            sub_table_name_full = f"{main_table_name}_{sub_table_name}"
            create_table_sql = f"CREATE TABLE IF NOT EXISTS {sub_table_name_full} (data TEXT);"
            create_table(db_conn, create_table_sql)

            sub_records = [{"data": json.dumps(row)} for row in sub_table_data]
            insert_data(db_conn, sub_table_name_full, [tuple(record.values()) for record in sub_records])
