# Python-Day-168-Email-Automation-System
# Python Day 168 – Email Automation System

## Project Description
A Python-based email automation system that reads recipient details from a CSV file and sends personalized emails using SMTP.

## Features
- Read recipients from a CSV file
- Validate basic email format
- Personalize messages using recipient names
- Send emails using Gmail SMTP
- Handle individual sending errors
- Store credentials in environment variables

## Technologies Used
- Python
- CSV
- SMTP
- EmailMessage
- Environment Variables

## Files
- `email_automation.py` – Main Python program
- `recipients.csv` – Recipient details

## How to Run
1. Create `recipients.csv` with name and email columns.
2. Configure your Gmail address and App Password as environment variables.
3. Run `python email_automation.py`.
4. Review the recipient list and confirm sending.

## Security Note
Use an App Password instead of your normal Gmail password. Send only to people who have agreed to receive your emails. Keep credentials private.

## Concepts Learned
CSV handling, SMTP, email automation, environment variables, functions and exception handling.
