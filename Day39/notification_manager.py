from twilio.rest import Client

TWILIO_SID = "ACcd4572ca0dfdff030febe1ba0ac1c38f"
TWILIO_AUTH_TOKEN= "1ec4a21d209edafbc407fa25bb034ddc"
TWILIO_VIRTUAL_NUMBER = "+18135319602"
TWILIO_VERIFIED_NUMBER = "+19293919331"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,

        )
        print(message.sid)