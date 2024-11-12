# Serverless Architecture Experiment Report

This repository documents an experiment using **AWS Lambda** for an automated email notification function. The function sends an email when a task is completed, showcasing serverless architecture's scalability, cost-efficiency, and ease of maintenance. Below, you'll find a detailed explanation of each part of the setup, execution, and testing of this serverless function.

---

## Table of Contents

- [Objective](#objective)
- [Architecture](#architecture)
- [Function Explanation](#function-explanation)
- [Setup and Configuration](#setup-and-configuration)
  - [Step 1: Environment Variables](#step-1-environment-variables)
  - [Step 2: Deployment](#step-2-deployment)
  - [Step 3: Execution](#step-3-execution)
  - [Step 4: Logs and Verification](#step-4-logs-and-verification)
  - [Step 5: Email Verification](#step-5-email-verification)
- [Conclusion](#conclusion)

---

## Objective

The objective of this experiment was to develop a serverless function using **AWS Lambda** to send an automated email notification upon task completion, while highlighting the advantages of serverless architecture in terms of scalability, cost management, and reduced maintenance.

---
## Architecture
The architecture for this serverless function follows a simple, event-driven design, utilizing AWS services to manage tasks with minimal infrastructure maintenance.

![a](https://github.com/user-attachments/assets/cf7908af-ce76-4850-ad6c-64325d28fcf6)

---

## Function Explanation

This function, named [lambda_function.py](lambda_function.py), is designed to send an automated email notification using the **smtplib** library to connect to an SMTP server and send an email.

### Step-by-Step Breakdown

1. **Environment Variables Setup**: 
   - The environment variables `SMTP_USER`, `SMTP_PASS`, `SENDER_EMAIL`, `RECIPIENT_EMAIL`, `SMTP_SERVER`, and `SMTP_PORT` are retrieved for secure SMTP credentials.
   
2. **Email Content Setup**: 
   - Define the subject and body of the email.

3. **Email Message Creation**: 
   - Create a MIME-compliant email message with the subject, sender, recipient, and body.

4. **SMTP Connection and Email Sending**: 
   - Connect to the SMTP server, log in, and send the email with encryption.

5. **Success Response**: 
   - If successful, the function returns a JSON response with a `statusCode` of 200.

6. **Error Handling**: 
   - Handle any errors that might occur during the email-sending process, including SMTP-specific errors.

---

## Setup and Configuration

### Step 1: Environment Variables
1. Go to the **AWS Lambda Console**.
2. In the **Environment Variables** section, add `SMTP_USER`, `SMTP_PASS`, `SENDER_EMAIL`, `RECIPIENT_EMAIL`, `SMTP_SERVER`, and `SMTP_PORT`.

### Step 2: Deployment
1. **Function Code**: Deploy the code by pasting it directly in the Lambda console editor or using a deployment package.
2. Save and deploy the function.

### Step 3: Execution
1. Use the **Test** feature in the Lambda console to manually trigger the function.
2. Create a test event, execute, and check for a successful email send.

### Step 4: Logs and Verification
1. Go to **AWS CloudWatch Console**.
2. Check the logs to verify successful execution.

### Step 5: Email Verification
1. Check the inbox of the recipient email account to verify receipt of the notification.


---

## Conclusion

This serverless function demonstrated AWS Lambda's effectiveness for small, event-driven tasks like email notifications. The serverless architecture proved advantageous by providing automatic scaling, cost efficiency, and maintenance-free infrastructure, making it ideal for on-demand, automated email notifications.

This setup is especially useful for tasks that need rapid execution without constant resource consumption, highlighting the flexibility and effectiveness of serverless computing.
