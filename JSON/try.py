# Find the name of the person who works in a <user-input> company

import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

user_data = json.loads(response.text)

search = input('Company Name: ')
def find_name(data):
    for user in data:
        name = user['company']['name']
        if (name == search):
            print(user['name'])

find_name(user_data)