from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog_Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_content= db.Column(db.String(255))
    
    def __init__(self,blog_title,blog_content):
        self.blog_title = blog_title
        self.blog_content = blog_content
   

@app.route('/', methods=['POST'])
def index():
    
    blog_list= Blog_Post.query.all()
    
    return render_template('blog-main-page.html',blog_list=blog_list)
@app.route('/blog', methods=['POST','GET'])
def build_blog():
    id_blog = request.args.get('id')
    blog_post = Blog_Post.query.get(id_blog)
   

    return render_template('blog.html',blog_post=blog_post)
@app.route('/add-blog-post',methods=['POST','GET'])
def add_blog():
    encoded_error = request.args.get("error")
    if request.method == 'POST':
        blog_title = request.form['blog-title']
        blog_body = request.form['blog-body']
        
        new_blog_post = Blog_Post(blog_title,blog_body)
        db.session.add(new_blog_post)
        db.session.commit()
        blog_list = Blog_Post.query.all()
        return render_template('blog-main-page.html',blog_list=blog_list)

    
    return render_template('add-post.html')

if __name__=='__main__':
    app.run()