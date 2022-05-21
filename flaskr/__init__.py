
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
# p.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://hvromtczbzsibl:8fe161f4ec7fa13418527862779859eccc556f3c7ca78726cb8f0519726ca024@ec2-52-54-212-232.compute-1.amazonaws.com:5432/d4tr3jqns7frbv'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='shdtee33gddg6djjguigfffvd@ft'
db=SQLAlchemy(app)
migrate=Migrate(app,db)
app.config['SECRET_KEY']='shfrfkenvrdgdg6djssdedjguigv@ft'


from . import app
