import pyarrow as pa 
import pyarrow.parquet as pq 
import os 


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/dezm_mage_cred_keys.json"

bucket_name = 'dezm-mage-01'
project_id = "resonant-time-434823-n0"

table_name = "nyc_taxi_data"

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    #column to parition on
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date

    #
    table = pa.Table.from_pandas(data)

    #letting know pyarrow the file system
    gcs = pa.fs.GcsFileSystem()

    #command to wrtite the partitioned dataset
    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols=['tpep_pickup_date'],
        filesystem = gcs
    )