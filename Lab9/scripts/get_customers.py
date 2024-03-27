import requests

api_url = 'http://localhost:8000/api/customers/'

token = '4c97672fc96e67c9011d3938a51aea720d6cc185'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url,headers=headers)

print(response.status_code)


if response.status_code == 200:
    print(f"Customers retrieval successful. {response.text}")
else:
    print(f"Customers retrieval failed. {response.text}")