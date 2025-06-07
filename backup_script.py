import ibm_boto3
from ibm_botocore.client import Config, ClientError

# IBM Cloud Object Storage Configuration
cos = ibm_boto3.client(
    's3',
    ibm_api_key_id="w0CXSEKlJ4EPFNMqOJYXZnznV5tGP78RW55rQBcKuwNJ",  # Replace with your actual API Key
    ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/11b3a63e3ec341799238a22d68fc81d3:64f7f44c-cd34-464a-9f16-96e0fadc7031:bucket:sindhu-test-bucket",  # Replace with your instance ID
    config=Config(signature_version="oauth"),
    endpoint_url="https://s3.au-syd.cloud-object-storage.appdomain.cloud"  # Replace <region>
)

def backup_file(file_path, bucket_name, object_name):
    """
    Uploads a file to IBM Cloud Object Storage.
    """
    try:
        cos.upload_file(Filename=file_path, Bucket=bucket_name, Key=object_name)
        print(f"✅ File '{file_path}' uploaded successfully as '{object_name}'.")
    except ClientError as e:
        print(f"❌ Error uploading file: {e}")

# Example Usage
if __name__ == "__main__":
    file_path = "C:\\Users\\Dell\\OneDrive\\Desktop\\testing.txt"  # Replace with the path to your file
    bucket_name = "sindhu-test-bucket"  # Your IBM Cloud bucket name
    object_name = "testing.txt"  # Name of the file in storage

    backup_file(file_path, bucket_name, object_name)
