# import packages
from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/users/ray/dev/zds/keys/zdsdatamatch00-8d8773db6af7.json'

# define function that downloads a file from the bucket
def download_cs_file(bucket_name, file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_file_name)

    return True

download_cs_file('zde_demo_test_storage_bucket', 'sample_data_1.csv', '../../../fixtures/sample_data_1_download.csv')