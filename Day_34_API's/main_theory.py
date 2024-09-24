import requests

#how to get a response from a json link 
response= requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)

response.raise_for_status()