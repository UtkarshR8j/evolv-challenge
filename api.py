from flask import Flask ,request,json
from flask_restful import Api,Resource
import blog_id
from .. import crud_db
#app=Flask(__name__)

app.config.from_pyfile('config.py')

@app.route("/",methods=['GET','POST'])
def index():
    return request.method

@app.route('/allblogs',methods=['GET']) 
def get_all_blog():
    allblogs=blog_id.query.all()
    blogs=blog_id_schema.dump(allblogs)
    return make_response(jsonify({"blogs":blogs}))


if __name__== '__main__':
    app.run()

