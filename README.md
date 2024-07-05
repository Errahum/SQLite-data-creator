# SQLite data creator

SQLite data creator is a Python application that allows users to manage SQLite databases through a user-friendly graphical interface built with Tkinter. This application enables users to create and open SQLite databases, create tables, load data from json, csv and Parquet files, display table contents, and drop tables as needed.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Resources](#resources)
- [Contribute](#contribute)
- [License](#license)
- [Donate](#donate)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6 or later.
- You have a basic understanding of SQLite databases.
- You have the following Python packages installed:
  - `tkinter`
  - `pandas`
  - `pyarrow`

## Installation

To install SQLite Manager, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sqlite-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd sqlite-manager
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use SQLite Manager, follow these steps:

1. Run the application:
    ```bash
    python sqlite_manager.py
    ```

2. Use the GUI to create or open an SQLite database, create tables, load data from json, csv and Parquet files, and manage tables.

### GUI Components

- **Database Frame**: Input the database file name and click "Open/Create" to open or create a database.
- **Table Frame**: Used for displaying available tables.
- **Insert Frame**: Select a json, csv or Parquet file to load data into the database.
- **Drop Table Button**: Delete the selected table.
- **Table Listbox**: Displays the list of tables in the database.
- **Data Text**: Displays the content of the selected table.

## Resources

For more information on SQLite and Tkinter, you can refer to the following resources:
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Contribute

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Donate

If you find this project helpful, consider supporting us with a donation to help maintain and improve the project. Thank you!

[![learning_application](https://i.imgur.com/abEFO5o.png)](https://buymeacoffee.com/sahurows)
