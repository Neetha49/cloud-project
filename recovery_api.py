from flask import Flask, jsonify
import ibm_boto3
from ibm_botocore.client import Config, ClientError

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running! Available routes: /restore/sindhu_test/sample.txt"}), 200

if __name__ == "__main__":
    app.run(debug=True)

# IBM Cloud Object Storage Configuration
cos = ibm_boto3.client(
    's3',
    ibm_api_key_id="w0CXSEKlJ4EPFNMqOJYXZnznV5tGP78RW55rQBcKuwNJ",  # Your API key
    ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/11b3a63e3ec341799238a22d68fc81d3:64f7f44c-cd34-464a-9f16-96e0fadc7031:bucket:sindhu-test-bucket",  # Your instance ID
    config=Config(signature_version="oauth"),
    endpoint_url="https://s3.au-syd.cloud-object-storage.appdomain.cloud"  # Update region if needed
)

@app.route('/restore/sindhu-test-bucket/testing.txt', methods=['GET'])
def restore_file(bucket_name, file_name):
    """
    Restores a file from IBM Cloud Object Storage.
    """
    try:
        local_path = f"restored_{file_name}"
        cos.download_file(bucket_name, file_name, local_path)
        return jsonify({"message": f"✅ File '{file_name}' restored successfully to '{local_path}'."})
    except ClientError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
