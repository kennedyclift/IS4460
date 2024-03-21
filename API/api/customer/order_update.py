import requests
import json

api_url = 'https://localhost:8000/api/orders/'  

order_id = 1  

updated_order_data = {
    "customer": 1,  
    "order_date": "2024-03-25",  
    "total_amount": 100.50  
}

response = requests.put(f'{api_url}{order_id}/', data=json.dumps(updated_order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Order updated successfully.")
else:
    print(f"Error updating order: {response.status_code} - {response.text}")
