import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = "sumthiingwong"
s3_prefix = "backups/"          # folder inside the bucket
restore_folder = "backup_files" # local folder to restore into

# Ensure the restore folder exists
os.makedirs(restore_folder, exist_ok=True)

# Restore files from S3 backups
def restore_files():
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_prefix).get("Contents", [])
    if not objects:
        print("⚠️ No files found in S3 backup folder.")
        return

    for obj in objects:
        key = obj["Key"]
        filename = key.replace(s3_prefix, "")  # remove 'backups/' prefix
        if filename:  # skip empty folder marker
            local_path = os.path.join(restore_folder, filename)
            s3.download_file(bucket_name, key, local_path)
            print(f"Restored {filename} to {restore_folder}/")

if __name__ == "__main__":
    restore_files()
