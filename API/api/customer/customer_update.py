import requests
import json

api_url = 'https://localhost:8000/api/customers/'  

customer_id = 1  

updated_customer_data = {
    "name": "Updated Customer Name",  
    "email": "updated_email@example.com",  
    "phone_number": "1234567890"  
}

response = requests.put(f'{api_url}{customer_id}/', data=json.dumps(updated_customer_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Customer updated successfully.")
else:
    print(f"Error updating customer: {response.status_code} - {response.text}")
