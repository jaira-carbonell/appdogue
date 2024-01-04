from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'projectdb'

mysql = MySQL(app)

# Import routes
from flaskapp import routes
