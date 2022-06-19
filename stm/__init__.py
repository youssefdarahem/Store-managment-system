import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
password = os.environ['DB_PASSWORD']
dburl = f"postgresql://postgres:{password}@localhost:5432/store"
print(dburl)
app.config['SQLALCHEMY_DATABASE_URI'] = dburl
app.config['SECRET_KEY'] = '736b6d99336f95a8b5a7b603d2e52cf5'
db = SQLAlchemy(app)


from stm import routes