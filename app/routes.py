from flask import render_template, redirect, url_for, request
from app import app
import sqlite3

@app.route('/')
def index():
    return render_template('brand_story.html')

@app.route('/products')
def product_list():
    conn = sqlite3.connect('perfume.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, brand, image_url, COALESCE(views, 0) FROM perfume ORDER BY COALESCE(views, 0) DESC")
    products = cursor.fetchall()
    conn.close()
    return render_template('product_list.html', products=products, collection_name='Les parfums')

@app.route('/hot')
def hot_product_list():
    page = request.args.get('page', 1, type=int)
    per_page = 4
    conn = sqlite3.connect('perfume.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM perfume WHERE popularity='high' ORDER BY COALESCE(views, 0) DESC")
    products = cursor.fetchall()
    conn.close()
    start = (page - 1) * per_page
    end = start + per_page
    products_to_show = products[start:end]
    has_next = end < len(products)
    return render_template(
        'hot_product_list.html',
        products_to_show=products_to_show,
        page=page,
        has_next=has_next
    )

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    conn = sqlite3.connect('perfume.db')
    cursor = conn.cursor()
    # 更新觀看次數
    cursor.execute("UPDATE perfume SET views = COALESCE(views, 0) + 1 WHERE id = ?", (product_id,))
    conn.commit()
    # 查詢商品資料（包含 views 欄位）
    cursor.execute("SELECT id, name, brand, image_url, accord, popularity, gender, product_url, COALESCE(views, 0) FROM perfume WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return render_template('product_detail.html', product=product)

@app.route('/brand_story')
def brand_story():
    return render_template('brand_story.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/men')
def men_perfume_list():
    conn = sqlite3.connect('perfume.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, brand, image_url FROM perfume WHERE gender='male'")
    products = cursor.fetchall()
    conn.close()
    return render_template('product_list.html', products=products,collection_name='Parfum pour homme')

@app.route('/women')
def women_perfume_list():
    conn = sqlite3.connect('perfume.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, brand, image_url FROM perfume WHERE gender='female'")
    products = cursor.fetchall()
    conn.close()
    return render_template('product_list.html', products=products,collection_name='Parfum pour femme')

