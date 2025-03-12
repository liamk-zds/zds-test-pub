# Sample code from https://github.com/RekhuGopal/PythonHacks/tree/main/GCP_Storage_Bucket_Handling_With_Python

# Prior to import, do this: pip install google-cloud-storage in the machine that you are running.
from google.cloud import storage
import os

# set key credentials file path. os.environ in python is a mapping object that represents the user's 
# OS environment variables. It returns a dictionary having the user's environment varialbe as key
# and their values as value.

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/users/ray/dev/zds/keys/zdsdatamatch00-8d8773db6af7.json'

def create_bucket(bucket_name, storage_class='STANDARD', location='australia-southeast1'): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
   
    bucket = storage_client.create_bucket(bucket, location=location) 
    # for dual-location buckets add data_locations=[region_1, region_2]
    
    return f'Bucket {bucket.name} successfully created.'

## Invoke Function
print(create_bucket('zde_demo_test_storage_bucket', 'STANDARD', 'australia-southeast1'))