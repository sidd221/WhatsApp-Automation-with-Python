from twilio.rest import Client
from datetime import datetime, timedelta #to calculate time difference
import time

account_sid = 'get your own id from twilio.com'
auth_token = 'same get it from twilio.com'
client = Client(account_sid, auth_token)

def send_sms(recipent_number, message_body):
    try:
        message = client.messages.create(
        from_='whatsapp: your twilio whatsapp number',
        body=message_body,
        to=f'whatsapp:{recipent_number}'
        )
        print(f'Message sent successfully! Message SID {message.sid}')
    except Exception as e:
        print(f'Failed to send message: {e}')

name = input("Enter your name: ")
phone_number = input("Enter your phone whatsapp number (with country code): ")
message_body = input("Enter the message you want to send to {name}: ")

date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()
time_difference = (scheduled_datetime - current_datetime).total_seconds()

if time_difference > 0:
    print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")
    time.sleep(time_difference)
    send_sms(phone_number, message_body)
else:
    print("The scheduled time is in the past. Please enter a future date and time.")