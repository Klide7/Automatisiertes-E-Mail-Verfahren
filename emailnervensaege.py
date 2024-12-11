import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
from dotenv import load_dotenv
import os

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv("email.env")

# Konfigurationsdaten aus Umgebungsvariablen
smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("PORT"))
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Nachrichtendetails
subject = "HEY fühl dich nicht genervt XD"

# Nachricht Variationen
message_variants = [
    "DU HOFFST DAS WAR DIE LETZTE ? XD",
    "Test",
    "KEINE ANGST KOMMEN NOCH MEHR XD",
]

# Anzahl der Nachrichten
total_emails = 100  # E-Mails senden

# Zeitintervall: Pausen zwischen den E-Mails
min_interval = 30  # 30 Sekunden
max_interval = 60  # 60 Sekunden

try:
    # SMTP-Verbindung aufbauen
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Verbindung sichern
    server.login(sender_email, password)  # Login mit App-spezifischem Passwort

    for i in range(total_emails):
        # Nachricht erstellen
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        body = random.choice(message_variants)  # Zufällige Variante der Nachricht
        message.attach(MIMEText(body, "plain"))

        # E-Mail senden
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"E-Mail {i+1} gesendet mit Text: '{body}'")

        # Zufällige Wartezeit
        if i < total_emails - 1:  # Nicht warten nach der letzten E-Mail
            wait_time = random.randint(min_interval, max_interval)
            print(f"Warte {wait_time} Sekunden, bevor die nächste E-Mail gesendet wird...")
            time.sleep(wait_time)

    print("Alle E-Mails erfolgreich gesendet!")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
finally:
    server.quit()
