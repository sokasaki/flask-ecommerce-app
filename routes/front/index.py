from app import app,render_template
from utils.api_helper import api_helper
import logging

logger = logging.getLogger(__name__)


@app.route('/')
@app.route('/home')
def home():
    products = api_helper.get_products()
    products = products[:4]  # Display only the first 4 products on the home page
    return render_template("front/index.html", products=products)