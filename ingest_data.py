#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df = pd.read_parquet("green_tripdata_2023-01.parquet")

df.head(0).to_sql(con=engine, name= "ny_taxi_data", if_exists='replace')

parquet_file = pq.ParquetFile("green_tripdata_2023-01.parquet")

chunk_size=10000
for batch in parquet_file.iter_batches(batch_size=chunk_size):
    start_time = time()
    df = batch.to_pandas()
    df.to_sql(con=engine, name= "ny_taxi_data", if_exists='append')
    end_time = time()
    print("inserting data chunk by chunk...it took %.3f second" %(end_time-start_time))
