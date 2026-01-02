import requests
from email_utils import send_email_alert

url = "https://dentalopolis.com"

response = requests.get(url)

if response.status_code == 200:
    print("The website is up and running!")

else:
    print("The website is down!")
    subject = f"[ALERT] Website Down - {url}"
    body = f"The website check failed with a status code: {response.status_code}"
    send_email_alert(subject, body)




