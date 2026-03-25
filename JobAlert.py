import requests
from twilio.rest import Client

acc_SID = "******************"
auth_token = "****************"

client = Client(acc_SID, auth_token)

recipients = [
    'whatsapp:**********',
    'whatsapp:**********'
]

url = "https://remoteok.com/api"

jobs = requests.get(url).json()

for job in jobs:
    if isinstance(job, dict):

        title = job.get("position", "")

        if "java" in title.lower() or "python" in title.lower() or "engineer" in title.lower():

            message = f"""JOB ALERT!!!
Company: {job.get('company')}
Role: {title}
Link: {job.get('url')}
"""

            for number in recipients:
                client.messages.create(
                    from_='whatsapp:**************',
                    body=message,
                    to=number
                )

            print("MESSAGE SENT TO ALL")
            break