import smtplib
from email.mime.text import MIMEText

def send_alert_email(subject, body, recipient_email="doctor@example.com"):
    """Send an email alert to notify discomfort or abnormal activities."""
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

if __name__ == "__main__":
    send_alert_email("Patient Alert", "A patient is showing signs of discomfort!")
