import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import fastavro
import os
from sqlalchemy import create_engine, inspect
import schedule
import time

# Source and destination DB URIs (e.g., PostgreSQL, MySQL, SQLite)
source_db = 'sqlite:///source.db'
dest_db = 'sqlite:///destination.db'

src_engine = create_engine(source_db)
dest_engine = create_engine(dest_db)

def export_all_tables():
    inspector = inspect(src_engine)
    tables = inspector.get_table_names()

    os.makedirs('exports', exist_ok=True)

    for table in tables:
        df = pd.read_sql_table(table, src_engine)

        # Export CSV
        df.to_csv(f"exports/{table}.csv", index=False)

        # Export Parquet
        table_parquet = pa.Table.from_pandas(df)
        pq.write_table(table_parquet, f"exports/{table}.parquet")

        # Export Avro
        records = df.to_dict(orient='records')
        schema = {
            'doc': f'{table} schema',
            'name': f'{table}_record',
            'namespace': 'example.avro',
            'type': 'record',
            'fields': [{'name': col, 'type': 'string'} for col in df.columns]
        }
        with open(f"exports/{table}.avro", 'wb') as out:
            fastavro.writer(out, schema, records)

    print("Export completed.")

def copy_all_tables():
    inspector = inspect(src_engine)
    tables = inspector.get_table_names()

    for table in tables:
        df = pd.read_sql_table(table, src_engine)
        df.to_sql(table, dest_engine, if_exists='replace', index=False)

def copy_selected_tables():
    table_columns = {
        'users': ['id', 'name', 'email'],
        'orders': ['order_id', 'user_id', 'amount']
    }

    for table, cols in table_columns.items():
        col_str = ', '.join(cols)
        query = f"SELECT {col_str} FROM {table}"
        df = pd.read_sql_query(query, src_engine)
        df.to_sql(table, dest_engine, if_exists='replace', index=False)

def full_pipeline():
    export_all_tables()
    copy_all_tables()
    copy_selected_tables()

# Schedule: run every day at 2:00 AM
schedule.every().day.at("02:00").do(full_pipeline)

print("Scheduler started. Waiting for trigger...")

while True:
    schedule.run_pending()
    time.sleep(10)
