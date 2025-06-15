from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def index():
    return render_template('base.html')  # 或你的首頁模板

@app.route('/account')
def account():
    user = {'name': '測試會員'}
    return render_template('account.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=5001)