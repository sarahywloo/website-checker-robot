import requests

url = "https://dentalopolis.com"

response = requests.get(url)

if response.status_code == 200:
    print("The website is up and running!")

else:
    print("The website is down!")


