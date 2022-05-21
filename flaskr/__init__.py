
from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY']='shfrfkenvrdgdg6djssdedjguigv@ft'


from . import app
