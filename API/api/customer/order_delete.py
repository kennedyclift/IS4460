import requests

api_url = 'http://localhost:8000/api/orders/1/'  

response = requests.delete(api_url)

if response.status_code == 204:
    print("Order deleted successfully.")
else:
    print("Error deleting order.")
