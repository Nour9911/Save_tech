import requests

# Define the URL to which you want to send the POST request
url = 'http://127.0.0.1:5000/backup'

# Send a POST request to the URL
response = requests.post(url)

# Print the response
print(response.text)
