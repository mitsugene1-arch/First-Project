🚀 Automated Cloud Backup & Recovery System
📌 Overview

This project is a beginner-friendly cloud automation tool that:

Backs up files from a local folder to AWS S3

Restores files back to the local machine when needed

Demonstrates practical skills in cloud storage, scripting, and automation

⚙️ Features

Backup local files to AWS S3 with one command

Restore files from S3 to your machine

Simple, menu-driven interface (Python CLI)

Automated scheduling via Windows Task Scheduler

Logging for backup and restore events

🛠️ Tech Stack

Python (boto3, os, datetime)

AWS S3 (cloud storage)

Windows Task Scheduler (automation)

🚀 Getting Started
1. Clone this repository
git clone https://github.com/mitsugene1-arch/First-Project.git
cd First-Project

2. Install dependencies
pip install boto3

3. Configure AWS CLI

Make sure you have AWS credentials set up:

aws configure

4. Run the script
python cloud_backup.py


Type 1 → Backup files

Type 2 → Restore files

🤖 Automation

To automate daily backups, create a .bat file:

echo 1 | python cloud_backup.py


Then schedule it using Windows Task Scheduler to run at a desired time.

📂 Project Structure
First-Project/
│-- cloud_backup.py     # Main script (backup + restore)
│-- backup.py           # Backup script only
│-- restore.py          # Restore script only
│-- cloud_menu.py       # Menu-driven CLI
│-- auto_backup.bat     # Example automation script
│-- README.md           # Project documentation
│-- backup_files/       # Local files to back up / restore

🎯 Why This Project?

This project highlights:

Cloud storage management with AWS S3

Python scripting for automation and recovery

Real-world IT support & cloud engineering skills

Experience with Windows automation (Task Scheduler)

🔮 Future Improvements

Add support for Google Cloud Storage and Azure Blob Storage

Implement encryption for secure backups

Add versioning to keep multiple file states in S3

Build a GUI interface for non-technical users

Send email or Slack notifications after successful backups/restores
