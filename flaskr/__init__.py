
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://leklkzbqbnefmu:448f5f698d6aa7a264ed288852452c0924b3a75edb05bc01d2b4f92f7408a4fe@ec2-52-3-2-245.compute-1.amazonaws.com:5432/dcep280bbmjp4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='shdtee33gddg6djjguigfdffvd@ft'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

app.config['SECRET_KEY']='shfrfkenvrdgdg6djsffsdedjguigv@ft'
