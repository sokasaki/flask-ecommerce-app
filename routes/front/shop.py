from app import app,render_template,requests,request,jsonify
# import requests


@app.get('/shop')
def shop():
    try:
        res = requests.get('https://fakestoreapi.com/products', timeout=10)
        res.raise_for_status()
        data = res.json()
        products = data
        
        # Get filter parameters from URL
        category_filter = request.args.get('category', 'all')
        search_query = request.args.get('search', '')
        
        # Filter products based on parameters
        if category_filter != 'all':
            products = [p for p in products if category_filter.lower() in p['category'].lower()]
        
        if search_query:
            products = [p for p in products if search_query.lower() in p['title'].lower() or search_query.lower() in p['category'].lower()]
    except Exception as e:
        print(f"Error fetching products: {e}")
        products = []
    
    return render_template("front/shop.html", products=products)

@app.route('/api/products/filter')
def filter_products():
    """API endpoint for filtering products"""
    try:
        res = requests.get('https://fakestoreapi.com/products', timeout=10)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        print(f"Error fetching products: {e}")
        return jsonify([])
    
    category = request.args.get('category', 'all')
    search = request.args.get('search', '')
    sort_by = request.args.get('sort', 'default')
    
    # Filter by category
    if category != 'all':
        if category == 'men':
            data = [p for p in data if "men's" in p['category'].lower()]
        elif category == 'women':
            data = [p for p in data if "women's" in p['category'].lower()]
        else:
            data = [p for p in data if category.lower() in p['category'].lower()]
    
    # Filter by search
    if search:
        data = [p for p in data if search.lower() in p['title'].lower() or search.lower() in p['category'].lower()]
    
    # Sort products
    if sort_by == 'price-asc':
        data.sort(key=lambda x: x['price'])
    elif sort_by == 'price-desc':
        data.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'name-asc':
        data.sort(key=lambda x: x['title'])
    elif sort_by == 'name-desc':
        data.sort(key=lambda x: x['title'], reverse=True)
    
    return jsonify(data)