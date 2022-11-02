import sqlite3
import os

def check_base(file_path: str) -> bool:
    return os.path.exists(file_path)

def create_base(file_path: str, sql_file: str) -> None:
    db = sqlite3.connect(file_path)
    cur = db.cursor()

    with open(sql_file, 'r') as sql_file:
        scripts = sql_file.read()

    for row in scripts.split(';'):
        try:
            cur.execute(row)
            db.commit()
        except sqlite3.Error as error:
            print(error)
            db.rollback()
    cur.close()
    db.close()