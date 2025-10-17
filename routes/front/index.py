from app import app,render_template,requests


@app.route('/')
@app.route('/home')
def home():
    res = requests.get('https://fakestoreapi.com/products')
    data = res.json()
    products = data[:4]  # Display only the first 4 products on the home page
    return render_template("front/index.html" , products=products)