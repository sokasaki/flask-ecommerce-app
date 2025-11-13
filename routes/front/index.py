from app import app,render_template,requests


@app.route('/')
@app.route('/home')
def home():
    try:
        res = requests.get('https://fakestoreapi.com/products', timeout=10)
        res.raise_for_status()
        data = res.json()
        products = data[:4]  # Display only the first 4 products on the home page
    except Exception as e:
        print(f"Error fetching products: {e}")
        products = []
    return render_template("front/index.html" , products=products)