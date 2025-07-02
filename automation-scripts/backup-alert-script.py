#!/usr/bin/env python3
"""
backup-alert-script.py
Monitors website backup status for qisetna.com and sends alert emails if backups are missing or outdated.
"""

import os
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta

# --- Configuration ---

# Folder where backups are stored
BACKUP_FOLDER = "/path/to/your/backup/folder"

# Minimum acceptable age of backup file (e.g., 24 hours)
MAX_BACKUP_AGE_HOURS = 24

# Email settings for alerts
ALERT_EMAIL_FROM = "alert@qisetna.com"
ALERT_EMAIL_TO = "info@qisetna.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your.email@gmail.com"  # Replace with your SMTP username
SMTP_PASSWORD = "your_app_password"     # Use app password or OAuth token if Gmail

# --- Helper Functions ---

def get_most_recent_backup():
    """Returns the path and modification time of the most recent backup file."""
    if not os.path.isdir(BACKUP_FOLDER):
        return None, None

    backup_files = [os.path.join(BACKUP_FOLDER, f) for f in os.listdir(BACKUP_FOLDER)]
    backup_files = [f for f in backup_files if os.path.isfile(f)]

    if not backup_files:
        return None, None

    most_recent = max(backup_files, key=os.path.getmtime)
    mod_time = datetime.fromtimestamp(os.path.getmtime(most_recent))

    return most_recent, mod_time

def send_alert_email(subject, body):
    """Sends an alert email."""
    msg = EmailMessage()
    msg["From"] = ALERT_EMAIL_FROM
    msg["To"] = ALERT_EMAIL_TO
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print("Alert email sent.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def check_backup_status():
    """Check if backup exists and is recent enough."""
    backup_file, mod_time = get_most_recent_backup()

    if backup_file is None:
        subject = "CRITICAL: No Backups Found for qisetna.com"
        body = f"No backup files found in {BACKUP_FOLDER}.\nImmediate action required!"
        send_alert_email(subject, body)
        return

    age = datetime.now() - mod_time
    if age > timedelta(hours=MAX_BACKUP_AGE_HOURS):
        subject = "WARNING: Outdated Backup for qisetna.com"
        body = (f"The most recent backup file ({os.path.basename(backup_file)}) is "
                f"{age.total_seconds() / 3600:.2f} hours old, which exceeds the threshold of "
                f"{MAX_BACKUP_AGE_HOURS} hours.\nPlease verify backup process.")
        send_alert_email(subject, body)
    else:
        print(f"Backup is recent: {os.path.basename(backup_file)}, modified at {mod_time}")

# --- Main Execution ---

if __name__ == "__main__":
    check_backup_status()

##Change BACKUP_FOLDER to the folder where your backups are stored.
##Adjust MAX_BACKUP_AGE_HOURS to define how fresh a backup must be to avoid alerts.
##Set your SMTP email credentials to send alert emails.
##Save this script as backup-alert-script.py in your automation-scripts/ folder.
##Make it executable:

chmod +x backup-alert-script.py
0 7 * * * /usr/bin/python3 /path/to/automation-scripts/backup-alert-script.py >> /var/log/backup-alert.log 2>&1
