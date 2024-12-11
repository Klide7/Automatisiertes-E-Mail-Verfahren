import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime
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

# Nachrichtendetails für die Ankunftsnachricht um 7 Uhr
arrival_subject = "Willkommen im Gästehaus Klide"
arrival_message = """Hallo,

schön, dass du im Gästehaus Klide angekommen bist! Wir hoffen, du hast eine angenehme Reise hinter dir.

Unser Frühstück gibt es ab 8 Uhr. Wir freuen uns auf dich!

Mit freundlichen Grüßen,
Das Team von Gästehaus Klide
"""

# Nachrichtendetails für die Vorschläge um 12 Uhr
activity_subject = "Vorschläge für Unternehmungen"
activity_message = """Hallo,

wir hoffen, du hast einen angenehmen Aufenthalt bei uns! Falls du noch nicht sicher bist, wie du deinen Tag gestalten möchtest, hier ein paar Vorschläge:

- Wanderung zum nahegelegenen Naturpark
- Stadtbesichtigung mit einem historischen Rundgang
- Entspannte Zeit in einem der lokalen Cafés

Viel Spaß bei der Entdeckung!

Mit freundlichen Grüßen,
Das Team von Gästehaus Klide
"""

def send_email(subject, body):
    try:
        # SMTP-Verbindung aufbauen
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Verbindung sichern
        server.login(sender_email, password)  # Login mit App-spezifischem Passwort

        # Nachricht erstellen
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # E-Mail senden
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"E-Mail gesendet: {subject}")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        server.quit()

# Hauptlogik: E-Mails zu den richtigen Zeiten senden
while True:
    current_time = datetime.now()

    # Um 7 Uhr die Ankunftsnachricht senden
    if current_time.hour == 7 and current_time.minute == 0:
        send_email(arrival_subject, arrival_message)
        print(f"Ankunftsnachricht gesendet um {current_time.strftime('%H:%M')}")
        time.sleep(60)  # Warten, damit es nicht jede Minute wiederholt wird

    # Um 12 Uhr mittags die Vorschläge senden
    if current_time.hour == 12 and current_time.minute == 0:
        send_email(activity_subject, activity_message)
        print(f"Vorschläge für Unternehmungen gesendet um {current_time.strftime('%H:%M')}")
        time.sleep(60)  # Warten, damit es nicht jede Minute wiederholt wird

    time.sleep(30)  # Alle 30 Sekunden überprüfen
