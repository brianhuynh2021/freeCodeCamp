from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)  
    