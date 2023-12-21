from dotenv import load_dotenv
import os
from connect import get_conn


def create_db():
    try:
        conn = get_conn("config/zno.env")
        cur = conn.cursor()

        conn.autocommit = True          #without this code string appears Error: DROP DATABASE cannot run inside a transaction block


        load_dotenv("config/zno_norm.env", override= True)
        database = os.getenv("DB_DATABASE")


        cur.execute(f"DROP DATABASE IF EXISTS {database};")
        cur.execute(f"CREATE DATABASE {database};")

        conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        print("eeeeeee")
        print(f"Error: {e}")

