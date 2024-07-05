import tkinter as tk

from data.output import sql_output
from src.sqlite_functions import select_file, open_create_db, load_file, drop_selected_table, update_table_list, \
    display_table_content


class SQLiteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQLite Manager")

        self.conn = None

        # Widgets pour créer/ouvrir la base de données
        self.db_frame = tk.Frame()
        self.db_frame.pack(pady=10)

        self.db_label = tk.Label(self.db_frame, text="Database:")
        self.db_label.pack(side=tk.LEFT)

        self.db_entry = tk.Entry(self.db_frame, width=30)
        self.db_entry.pack(side=tk.LEFT, padx=5)

        self.db_button = tk.Button(self.db_frame, text="Open/Create", command=self.open_create_db)
        self.db_button.pack(side=tk.LEFT)

        # Widgets pour créer une table
        self.table_frame = tk.Frame()
        self.table_frame.pack(pady=10)

        # Widgets pour insérer des données
        self.insert_frame = tk.Frame()
        self.insert_frame.pack(pady=10)

        self.file_button = tk.Button(self.insert_frame, text="Select File", command=self.select_file)
        self.file_button.pack(side=tk.LEFT, padx=5)

        # Bouton pour supprimer une table
        self.drop_table_button = tk.Button(text="Drop Table", command=self.drop_selected_table)
        self.drop_table_button.pack(pady=10)

        self.file_label = tk.Label(self.insert_frame, text="No file selected")
        self.file_label.pack(side=tk.LEFT, padx=5)

        # Listbox for displaying tables
        self.table_listbox = tk.Listbox(width=50, height=10)
        self.table_listbox.pack(pady=10)
        self.table_listbox.bind('<<ListboxSelect>>', self.display_table_content)

        # Text widget to display data
        self.data_text = tk.Text(wrap=tk.NONE)
        self.data_text.pack(pady=10)

        self.output_dir = sql_output

    def select_file(self):
        select_file(self)  # Importation de la fonction séparée

    def open_create_db(self):
        open_create_db(self)  # Importation de la fonction séparée

    def load_file(self, file_path, file_type):
        load_file(self, file_path, file_type)  # Importation de la fonction séparée

    def drop_selected_table(self):
        drop_selected_table(self)  # Importation de la fonction séparée

    def update_table_list(self):
        update_table_list(self)  # Importation de la fonction séparée

    def display_table_content(self, event):
        display_table_content(self, event)  # Importation de la fonction séparée
