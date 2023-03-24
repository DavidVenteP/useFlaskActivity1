from typing import List, Dict
from flask import Flask, render_template, send_from_directory
import json

from data import Articles

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

def my_articles() -> List[Dict]:
    articles = Articles()
    return articles

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/features')
def features():
    return render_template('features.html')
@app.route('/download')
def download():
    return render_template('download.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
