from flask import render_template, redirect, url_for
from app import app

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/products')
def product_list():
    return render_template('product_list.html')

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    return render_template('product_detail.html', product_id=product_id)

@app.route('/brand_story')
def brand_story():
    return render_template('brand_story.html')

@app.route('/account')
def account():
    return render_template('account.html')

