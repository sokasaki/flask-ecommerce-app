
from app import app, render_template,requests
from flask import request

@app.get('/detail')
def detail():
    try:
        res = requests.get('https://fakestoreapi.com/products', timeout=10)
        res.raise_for_status()
        data = res.json()
        products = data
    except Exception as e:
        print(f"Error fetching products: {e}")
        products = []
    product_name = request.args.get('product-title')
    return render_template('front/product-detail.html', module='detail', products=products)