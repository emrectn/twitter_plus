from flask import Flask, render_template, session, redirect
from app.views.user import bp as user_bp
from app.views.auth import bp as auth_bp
from app.views.post import bp as post_bp

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(post_bp)

# Session secret key
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/')
def index():
    if 'user' in session:
        return redirect('/user/profile')
    return render_template("index.html")
