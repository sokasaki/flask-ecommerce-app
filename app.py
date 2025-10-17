from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

import routes

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)