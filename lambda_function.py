import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def lambda_handler(event, context):
    try:
        # Retrieve environment variables
        smtp_user = os.environ['SMTP_USER']
        smtp_pass = os.environ['SMTP_PASS']
        sender_email = os.environ['SENDER_EMAIL']
        recipient_email = os.environ['RECIPIENT_EMAIL']
        smtp_server = os.environ['SMTP_SERVER']
        smtp_port = 587  # SES supports ports 25, 465, and 587

        # Set up email content
        subject = "Notification: Task Update"
        body = f"""Dear User,

This is an automated email notification regarding your task.

Status: Task Completed

Thank you,
Yashvi"""

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Establish SMTP connection and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_pass)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        # Success response
        return {
            'statusCode': 200,
            'body': "Email sent successfully!"
        }

    except smtplib.SMTPException as e:
        # Catch any SMTP related errors
        print(f"SMTP error occurred: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to send email due to SMTP error: {e}"
        }

    except Exception as e:
        # Catch any other errors
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to send email due to unexpected error: {e}"
        }"
