import requests

api_url = 'http://localhost:8000/api/orders/1/'  

response = requests.get(api_url)

if response.status_code == 200:
    order_data = response.json()
    print("Order details:")
    print(order_data)
else:
    print("Error getting order details.")
