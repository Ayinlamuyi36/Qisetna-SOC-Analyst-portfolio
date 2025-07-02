#!/usr/bin/env python3
"""
email-log-monitor.py
Monitors email sending logs for errors and reports issues for qisetna.com

This script can be run as a scheduled task (cron) to keep track of email problems.
"""

import os
import re
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta

# --- Configuration ---

LOG_FILE_PATH = "/var/log/mail.log"  # Path to your email sending log file (adjust as needed)
ERROR_PATTERN = re.compile(r"(error|fail|denied|reject|warning)", re.IGNORECASE)
LAST_RUN_FILE = "/tmp/email_log_monitor_last_run.txt"

ALERT_EMAIL_FROM = "alert@qisetna.com"
ALERT_EMAIL_TO = "info@qisetna.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your.email@gmail.com"  # Replace with your SMTP username
SMTP_PASSWORD = "your_app_password"     # Use app password or OAuth token if Gmail

# --- Helper Functions ---

def read_last_run_time():
    """Reads the last run timestamp from a file."""
    if not os.path.exists(LAST_RUN_FILE):
        # Default to 1 hour ago if no record exists
        return datetime.now() - timedelta(hours=1)
    with open(LAST_RUN_FILE, "r") as f:
        timestamp_str = f.read().strip()
        try:
            return datetime.fromisoformat(timestamp_str)
        except ValueError:
            return datetime.now() - timedelta(hours=1)

def write_last_run_time(timestamp):
    """Writes the last run timestamp to a file."""
    with open(LAST_RUN_FILE, "w") as f:
        f.write(timestamp.isoformat())

def send_alert_email(subject, body):
    """Sends an email alert about log issues."""
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

def monitor_log():
    """Monitors the email log for error entries since last run."""
    last_run_time = read_last_run_time()
    error_lines = []

    with open(LOG_FILE_PATH, "r") as logfile:
        for line in logfile:
            # Example log format check: adjust as needed based on your logs
            # Look for timestamp at start: 'Jun 27 10:22:45'
            try:
                log_time_str = " ".join(line.split()[:3])
                log_time = datetime.strptime(log_time_str, "%b %d %H:%M:%S")
                # Since year is missing, assume current year
                log_time = log_time.replace(year=datetime.now().year)
            except Exception:
                continue

            if log_time > last_run_time and ERROR_PATTERN.search(line):
                error_lines.append(line.strip())

    if error_lines:
        subject = f"Email Delivery Errors Detected on qisetna.com ({len(error_lines)} incidents)"
        body = "The following email delivery issues were detected:\n\n" + "\n".join(error_lines)
        send_alert_email(subject, body)
    else:
        print("No new email errors detected.")

    write_last_run_time(datetime.now())

# --- Main Execution ---

if __name__ == "__main__":
    monitor_log()

## How to Use
##Adjust LOG_FILE_PATH to point to the correct email log file your server or WP Mail SMTP writes to.
##Set your SMTP credentials for sending alert emails.
##Save this script as email-log-monitor.py in your automation-scripts/ folder.
##Make it executable:

chmod +x email-log-monitor.py
##Run it manually or set up a cron job to run it every 5-15 minutes:
*/10 * * * * /usr/bin/python3 /path/to/automation-scripts/email-log-monitor.py >> /var/log/email-log-monitor.log 2>&1
