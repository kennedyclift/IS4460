import requests

url = "http://localhost:8000/api-token-auth/"

credentials = {
    'username': 'can',
    'password': 'legogoat7'
}

response = requests.post(url,data=credentials)

if response.status_code ==200:
    token_data = response.json()
    
    print('token_data', token_data)

    token = token_data.get('token')

    if token:
        print(f"Authentication successful. Token: {token} ")
    else:
        print(f"Token not found in response.")
else:
    print("Authentication failed. Status code: ", response.status_code)
    with open('logfile.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

