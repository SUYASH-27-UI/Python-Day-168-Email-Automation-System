import csv
import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def load_recipients(filename):
    recipients = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                email = row.get("email", "").strip()
                name = row.get("name", "").strip()

                if email and "@" in email:
                    recipients.append({
                        "name": name,
                        "email": email
                    })

    except FileNotFoundError:
        print("Recipients file not found.")

    return recipients


def create_message(sender, recipient, subject, body):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient["email"]
    message["Subject"] = subject

    personalized_body = body.replace(
        "{name}", recipient["name"] or "there"
    )

    message.set_content(personalized_body)
    return message


def send_emails(recipients, subject, body):
    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_APP_PASSWORD")

    if not sender or not password:
        print("Set EMAIL_ADDRESS and EMAIL_APP_PASSWORD first.")
        return

    print(f"\n{len(recipients)} recipient(s) loaded.")
    confirm = input("Send these emails? Type YES to continue: ")

    if confirm != "YES":
        print("Sending cancelled.")
        return

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(sender, password)

            for recipient in recipients:
                try:
                    message = create_message(
                        sender, recipient, subject, body
                    )
                    server.send_message(message)
                    print("Sent to:", recipient["email"])

                except Exception as error:
                    print("Failed:", recipient["email"], error)

    except Exception as error:
        print("SMTP connection failed:", error)


def main():
    print("===== EMAIL AUTOMATION SYSTEM =====")

    recipients = load_recipients("recipients.csv")

    if not recipients:
        print("No valid recipients found.")
        return

    print("\nLoaded recipients:")
    for recipient in recipients:
        print(recipient["name"], "-", recipient["email"])

    subject = input("\nEnter email subject: ")
    body = input("Enter email message (use {name} for personalization): ")

    send_emails(recipients, subject, body)


if __name__ == "__main__":
    main()
