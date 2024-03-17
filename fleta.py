import db

from flask import Flask, render_template

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
        "SELECT * FROM post"
    )
    return render_template('index.html', posts=posts)