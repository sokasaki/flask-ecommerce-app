import sys
import traceback

try:
    from app import app
    import routes
    
    with app.test_client() as client:
        print("Testing /cart route...")
        response = client.get('/cart')
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 500:
            print("\n=== ERROR DETECTED ===")
            print(response.data.decode('utf-8'))
            
except Exception as e:
    print(f"Exception occurred: {e}")
    traceback.print_exc()
