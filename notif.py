import os
import pandas as pd
from twilio.rest import Client
from dotenv import load_dotenv
import time

load_dotenv()

file_path = 'updated_data.csv'
data = pd.read_csv(file_path)

TEMPERATURE_THRESHOLD = 38.989
HUMIDITY_THRESHOLD = 81.26

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
recipient_number = os.getenv("RECIPIENT_NUMBER")

client = Client(account_sid, auth_token)

def send_whatsapp_message(to_number, message_body):
    message = client.messages.create(
        from_=twilio_number,
        body=message_body,
        to=to_number
    )
    print(f"Message sent to {to_number}: {message.body}")

for index, row in data.iterrows():
    temperature = row['Temperature']
    date = row['Date']
    time = row['Time']

    date_time = f"{date} {time}"

    if temperature > TEMPERATURE_THRESHOLD:
        message = f"ALERT: Temperature above {TEMPERATURE_THRESHOLD}°C at {date_time}"
        send_whatsapp_message(recipient_number, message)


for index, row in data.iterrows():
    humidity = row['Air Humidity']
    date = row['Date']
    time = row['Time']

    date_time = f"{date} {time}"

    if humidity > HUMIDITY_THRESHOLD:
        message = f"ALERT: Humidity above {HUMIDITY_THRESHOLD}% at {date_time}"
        send_whatsapp_message(recipient_number, message)

