
from app import app, render_template,requests
from flask import request

@app.get('/detail')
def detail():
    res = requests.get('https://fakestoreapi.com/products')
    data = res.json()
    products = data
    product_name = request.args.get('product-title')
    return render_template('front/product-detail.html', module='detail', products=products)