from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog_Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_content= db.Column(db.String(255))
    def __init__(self,blog_title,blog_content):
        blog_title.self =''
        blog_content.self = ''
    def get_blog_title(self):
        return blog_title.self
    def set_blog_title(self,new_blog_title):
        blog_title.self = new_blog_title
    def get blog_content(self)
        return blog_content.self
    def set_blog_content(self,new_blog_content)
        blog_content.self = new_blog_content

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('blog-main-page.html')
