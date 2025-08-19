import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, ClientError

# === Configuration ===
bucket_name = "my-backup-bucket-project1"   # replace with your bucket
s3_folder = "backups/"                      # S3 path prefix
backup_folder = "."                         # local folder to back up (current dir)
restore_folder = "restored_files"           # where restored files will go
log_file = "cloud_backup.log"               # log file name


# === Setup Logging ===
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message, level="info"):
    """Helper function: log to console and file"""
    if level == "error":
        logging.error(message)
        print(f"❌ {message}")
    elif level == "warning":
        logging.warning(message)
        print(f"⚠️ {message}")
    else:
        logging.info(message)
        print(f"✅ {message}")


# === Backup ===
def backup_files():
    if not os.path.exists(backup_folder):
        log_event(f"Backup folder not found: {backup_folder}", "error")
        return

    s3 = boto3.client("s3")

    try:
        files = os.listdir(backup_folder)
        if not files:
            log_event("No files found in backup folder to upload.", "warning")
            return

        for file in files:
            file_path = os.path.join(backup_folder, file)

            if os.path.isfile(file_path):
                s3_key = s3_folder + file
                print(f"⬆️ Uploading {file} ...")
                s3.upload_file(file_path, bucket_name, s3_key)
                log_event(f"Uploaded {file} to s3://{bucket_name}/{s3_key}")

        log_event("Backup complete!")

    except NoCredentialsError:
        log_event("AWS credentials not found. Run `aws configure` first.", "error")
    except ClientError as e:
        log_event(f"AWS Error: {e}", "error")


# === Restore ===
def restore_files():
    if not os.path.exists(restore_folder):
        os.makedirs(restore_folder)

    s3 = boto3.client("s3")

    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)

        if "Contents" not in response:
            log_event("No files found in S3 backup folder.", "warning")
            return

        for obj in response["Contents"]:
            key = obj["Key"]

            if key.endswith("/"):  # skip "folder" keys
                continue

            file_name = os.path.basename(key)
            local_path = os.path.join(restore_folder, file_name)

            print(f"⬇️ Restoring {file_name} ...")
            s3.download_file(bucket_name, key, local_path)
            log_event(f"Restored {file_name} from s3://{bucket_name}/{key}")

        log_event(f"Restore complete! Files are in: {restore_folder}")

    except NoCredentialsError:
        log_event("AWS credentials not found. Run `aws configure` first.", "error")
    except ClientError as e:
        log_event(f"AWS Error: {e}", "error")


# === Menu ===
if __name__ == "__main__":
    print("Cloud Backup & Restore")
    print("1. Backup files")
    print("2. Restore files")

    choice = input("Choose option (1/2): ").strip()

    if choice == "1":
        backup_files()
    elif choice == "2":
        restore_files()
    else:
        log_event("Invalid option. Please choose 1 or 2.", "error")
