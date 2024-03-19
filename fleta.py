import db

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='not-so-fast',
    DATABASE='./fleta.sqlite'
)
db.init_app(app)


@app.route('/')
def index():
    database = db.get_db()
    posts = database.execute(
        '''SELECT * 
        FROM post'''
    )
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    database = db.get_db()
    post = database.execute(
        '''SELECT * 
        FROM post 
        WHERE id = ?''',
        (post_id,)
    ).fetchone()
    if post is not None:
        return render_template('post.html', post=post)
    return redirect(url_for('index'))