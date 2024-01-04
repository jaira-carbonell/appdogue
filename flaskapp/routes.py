from flaskapp import app, mysql
# from flask import jsonify

# @app.route('/testconnection')
# def test_connection():
#     try:
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT 1")
#         return jsonify({"status": "Connected to the database"})
#     except Exception as e:
#         return jsonify({"status": "Connection failed", "error": str(e)})

from flaskapp import app
from flask import render_template

@app.route('/')
def index():
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM products")  # Assuming 'products' is your table name
       products = cursor.fetchall()
       print(products)
       cursor.close()
       return render_template('index.html', products=products)

