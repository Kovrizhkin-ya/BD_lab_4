import psycopg
import time
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine



def get_conn(envpath="config/zno.env"):

     load_dotenv(envpath, override=True)

     username = os.getenv("DB_USERNAME")
     password = os.getenv("DB_PASSWORD")
     database = os.getenv("DB_DATABASE")
     host = os.getenv("DB_HOST")
     port = os.getenv("DB_PORT")
     url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

     try:
          conn = psycopg.connect(url)
          return conn
     except:
          print("Reconnecting...")
          time.sleep(5)
          return get_conn(envpath)


def get_engine(envpath="config/zno.env"):

     load_dotenv(envpath, override=True)

     username = os.getenv("DB_USERNAME")
     password = os.getenv("DB_PASSWORD")
     database = os.getenv("DB_DATABASE")
     host = os.getenv("DB_HOST")
     port = os.getenv("DB_PORT")
     url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

     try:
          engine = create_engine(url, echo=False)
          return engine
     except:
          print("Reconnecting...")
          time.sleep(5)
          return get_conn(envpath)


