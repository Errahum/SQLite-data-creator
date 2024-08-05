import tkinter as tk
from tkinter import messagebox, filedialog
import os
from src.sql_lite.db_manager import create_connection, drop_table
from src.sql_lite.data_loader import load_data_to_db_all_tables


def select_file(app):
    file_paths = filedialog.askopenfilenames(filetypes=[("JSON, CSV and Parquet", "*.json;*.parquet;*.csv")])
    if file_paths:
        for file_path in file_paths:
            app.file_label.config(text=app.file_label.cget("text") + "\n" + file_path)
            file_type = file_path.split('.')[-1]
            load_file(app, file_path, file_type)


def open_create_db(app):
    db_file = app.db_entry.get().strip()
    
    if not db_file:
        # Open file save dialog if entry is empty
        db_file = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite files", "*.db")])
        
    if db_file and not db_file.endswith('.db'):
        db_file += '.db'
    
    if db_file:
        db_file = os.path.join(app.output_dir, db_file)
        app.conn = create_connection(db_file)
        
        if app.conn:
            messagebox.showinfo("Information", f"Connected to database: {db_file}")
            update_table_list(app)
        else:
            messagebox.showerror("Error", "Failed to connect to database.")
    else:
        messagebox.showerror("Error", "Invalid database file name.")


def load_file(app, file_path, file_type):
    if app.conn:
        app.data_text.delete(1.0, tk.END)
        if file_type.lower() in ['parquet', 'json', 'csv']:
            load_data_to_db_all_tables(app.conn, file_path, file_type)
            app.data_text.insert(tk.END, f"Data from {file_path} loaded successfully.")
            update_table_list(app)
        else:
            messagebox.showerror("Error", "Unsupported file type. Use 'parquet', 'json' or 'csv'.")
    else:
        messagebox.showerror("Error", "Database is not connected.")


def drop_selected_table(app):
    selection = app.table_listbox.curselection()
    if selection:
        table_name = app.table_listbox.get(selection[0])
        if table_name:
            if messagebox.askyesno("Confirmation", f"Are you sure you want to drop table '{table_name}'?"):
                if app.conn:
                    drop_table(app.conn, table_name)
                    update_table_list(app)
                    app.data_text.delete(1.0, tk.END)
                else:
                    messagebox.showerror("Error", "Database is not connected.")
    else:
        messagebox.showerror("Error", "No table selected.")


def update_table_list(app):
    if app.conn:
        app.table_listbox.delete(0, tk.END)
        cursor = app.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        master_table = None
        for table in tables:
            table_name = table[0]
            if table_name.endswith('_tables'):
                master_table = table_name
            else:
                app.table_listbox.insert(tk.END, table_name)
        if master_table:
            app.table_listbox.insert(0, master_table)


def display_table_content(app, event):
    if app.conn:
        selection = event.widget.curselection()
        if selection:
            table_name = event.widget.get(selection[0])
            cursor = app.conn.cursor()
            cursor.execute(f"SELECT * FROM \"{table_name}\"")
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            app.data_text.delete(1.0, tk.END)
            app.data_text.insert(tk.END, f"Table: {table_name}\n")
            app.data_text.insert(tk.END, f"Columns: {', '.join(columns)}\n")
            for row in rows:
                app.data_text.insert(tk.END, f"{row}\n")
