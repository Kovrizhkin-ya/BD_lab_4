from connect import get_engine
from sqlalchemy import MetaData
import pandas as pd


def get_table(table_name, envpath):
    engine = get_engine(envpath)
    con = engine.connect()

    table = pd.read_sql_table(table_name, con)
    return table


def get_tables(envpath):
    engine = get_engine(envpath)

    metadata = MetaData()
    metadata.reflect(bind=engine)
    dict_keys_object = metadata.tables.keys()
    table_names = list(dict_keys_object)
    df = {}

    for table_name in table_names:
        df[table_name] = get_table(table_name, envpath)

    return df





#print(get_tables("config/zno_norm.env"))
