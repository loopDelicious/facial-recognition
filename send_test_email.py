import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from dotenv import load_dotenv
load_dotenv()

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email(os.environ.get('SENDGRID_EMAIL'))  # Change to your verified sender
to_email = To(os.environ.get('RECIPIENT_EMAIL'))  # Change to your recipient
subject = "You have a visitor"
content = Content("text/plain", "Your webcam recognizes someone.")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)