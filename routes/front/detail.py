
from app import app, render_template
from flask import request
from utils.api_helper import api_helper
import logging

logger = logging.getLogger(__name__)

@app.get('/detail')
def detail():
    products = api_helper.get_products()
    product_name = request.args.get('name') or request.args.get('product-title')
    
    # Find the specific product by title
    product = None
    if product_name and products:
        # URL decode the name in case it comes encoded
        from urllib.parse import unquote
        decoded_name = unquote(product_name)
        product = next((p for p in products if p.get('title') == decoded_name), None)
    
    # If not found by title, try by ID
    if not product:
        product_id = request.args.get('id')
        if product_id and products:
            try:
                product = next((p for p in products if p.get('id') == int(product_id)), None)
            except (ValueError, TypeError):
                pass
    
    # If still no product found, use first product or empty dict
    if not product:
        product = products[0] if products else {}
    
    return render_template('front/product-detail.html', module='detail', product=product, products=products)