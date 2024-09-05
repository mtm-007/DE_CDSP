#!/usr/bin/env python
# coding: utf-8

import os,sys
import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time
import argparse

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    table_name = params.table_name
    url = params.url

    file_name = 'output.parquet'
    #download the data
    os.system(f"wget {url} -O {file_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

    parquet_file = pq.ParquetFile(file_name)

    chunk_size=100000
    for batch in parquet_file.iter_batches(batch_size=chunk_size):
        start_time = time()
        df = batch.to_pandas()
        df.to_sql(con=engine, name= table_name, if_exists='append')
        end_time = time()
        print("inserting data chunk by chunk...it took %.3f second" %(end_time-start_time))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest data to postgres.')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host declaration for postgres')
    parser.add_argument('--port', help='port number for postgres')
    parser.add_argument('--dbname', help='database name for postgres')
    parser.add_argument('--table_name', help='name for the table were the results be written on postgres')
    parser.add_argument('--url', help='url for the data needed to load in to postgres')

    args = parser.parse_args()

    main(args)

