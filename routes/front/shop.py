from app import app,render_template,requests
# import requests


@app.get('/shop')
def shop():
    res = requests.get('https://fakestoreapi.com/products')
    data = res.json()
    products = data
    return render_template("front/shop.html", products=products)