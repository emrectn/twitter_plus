from flask import Blueprint, request, redirect, session, render_template
from app.models import User, DBSession

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        db = DBSession()
        u = db.query(User).filter(User.username == username,
                                  User.password == password).first()

        if u:
            session['user'] = username
            session['id'] = u.id
            print("--{}-- kisisi oturum acit ".format(session['user']))
            return redirect('/user/profile')

        else:
            print("Yanlis kullanici sifresi veya adi")
            return redirect('/')


@bp.route('/logout')
def user_logout():
    if 'user' in session:
        print('-{}- kisisi cikis yapti'.format(session['user']))
        del session['user']
    else:
        print('Once Giris yapiniz')

    return redirect('/')
