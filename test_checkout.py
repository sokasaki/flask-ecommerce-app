from app import app
import routes

with app.test_client() as client:
    response = client.get('/checkout')
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.data.decode()}")
