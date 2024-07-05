import sqlite3
from sqlite3 import Error


# Ce module se chargera de la création et de la gestion des tables SQLite.

def create_connection(db_file):
    """ Crée une connexion à la base de données SQLite spécifiée par db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connexion réussie à SQLite: {db_file}")
    except Error as e:
        print(f"Erreur de connexion à SQLite: {e}")
    return conn


def create_table(conn, create_table_sql):
    """ Crée une table depuis la requête CREATE TABLE """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(f"Erreur lors de la création de la table: {e}")


def insert_data(conn, table, data):
    """ Insère des données dans une table """
    placeholders = ', '.join(['?' for _ in data[0]])
    sql = f"INSERT INTO {table} VALUES ({placeholders})"
    try:
        c = conn.cursor()
        c.executemany(sql, data)
        conn.commit()
    except Error as e:
        print(f"Erreur lors de l'insertion des données: {e}")


def drop_table(conn, table_name):
    """ Supprime une table de la base de données """
    sql = f"DROP TABLE IF EXISTS {table_name}"
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        print(f"Table {table_name} supprimée avec succès")
    except Error as e:
        print(f"Erreur lors de la suppression de la table {table_name}: {e}")
