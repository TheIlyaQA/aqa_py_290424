import sqlite3
import csv
def create_database(db_name: str):
    conn = sqlite3.connect(db_name)
    conn.close()


def create_table(db_name, table_name, columns):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Формуємо рядок з описом стовпців
    columns_str = ", ".join([f"{name} {data_type}" for name, data_type in columns.items()])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"

    # Виводимо запит для відладки
    print(f"Executing SQL: {create_table_query}")

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()


def insert_record(db_name, table_name, values):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    placeholders = ", ".join(["?" for _ in values])
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"

    cursor.execute(insert_query, values)
    conn.commit()
    conn.close()


def select_all_records(db_name, table_name):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()

    conn.close()
    return records

def delete_record(db_name, table_name, condition):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    delete_query = f"DELETE FROM {table_name} WHERE {condition}"
    cursor.execute(delete_query)
    conn.commit()
    conn.close()


