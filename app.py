from flask import Flask 
from config import Config
app=Flask(__name__)

app.config.from_object(Config)

@app.route("/",methods=['GET'])
def index():
    return "this is the app.py script"

if __name__== '__main__':
    app.run()