
from app import app, render_template
from flask import request
from utils.api_helper import api_helper
import logging

logger = logging.getLogger(__name__)

@app.get('/detail')
def detail():
    products = api_helper.get_products()
    product_name = request.args.get('product-title')
    return render_template('front/product-detail.html', module='detail', products=products)