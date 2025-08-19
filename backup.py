import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = "sumthiingwong"
backup_folder = "backup_files"
s3_prefix = "backups/"  # folder inside bucket

# Upload files from local folder to S3
def backup_files():
    for file in os.listdir(backup_folder):
        local_path = os.path.join(backup_folder, file)
        if os.path.isfile(local_path):
            s3.upload_file(local_path, bucket_name, f"{s3_prefix}{file}")
            print(f"Uploaded {file} to {bucket_name}/{s3_prefix}")

# Download files back from S3
def restore_files():
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_prefix).get("Contents", [])
    for obj in objects:
        key = obj["Key"]
        filename = key.replace(s3_prefix, "")  # remove prefix
        s3.download_file(bucket_name, key, f"restored_{filename}")
        print(f"Restored {filename} to local machine")

if __name__ == "__main__":
    print("1. Backup files\n2. Restore files")
    choice = input("Choose option: ")
    if choice == "1":
        backup_files()
    else:
        restore_files()