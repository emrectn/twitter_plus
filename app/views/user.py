from flask import Blueprint, request, redirect, session, render_template
from app.models import User, Post, DBSession

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/add', methods=['POST'])
def new_user():
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()
    # Database icin bir session oluşturuldu.
    db = DBSession()
    exists = db.query(User).filter(User.username == username).first()
    if not exists:
        u = User(username=username,
                 password=password,
                 status=1)
        db.add(u)
        db.commit()
        u = db.query(User).filter(User.username == username).first()
        session['id'] = u.id
        print(u.id)
        session['user'] = username
        db.close()

        print("{} kisisi kaydoldu".format(session['user']))
    else:
        print("\'{}\' kisisi zaten var".format(username))
        db.close()
    return redirect('/')


@bp.route('/remove', methods=['POST'])
def remove_user():
    username = request.form.get("username")
    password = request.form.get("password")

    db = DBSession()
    u = db.query(User).filter(User.username == username,
                              User.password == password).first()
    if u:
        db.delete(u)
        db.commit()
        print("-{}-kullanici Silindi".format(username))
    else:
        print("-{}-kullanici Silinemedi".format(username))
        db.close()

    return redirect('/')


@bp.route('/change_password', methods=['POST'])
def change_password():
    username = request.form.get("username")
    password = request.form.get("password")
    new_password = request.form.get("new_password")

    db = DBSession()
    u = db.query(User).filter(User.username == username,
                              User.password == password).first()

    if u:
        u.password = new_password
        db.commit()
        print("{} kisisinin sifresi Degistirildi".format(username))
    else:
        print("{} kisisinin sifresi Degistirilemedi".format(username))
        db.close()

    return redirect('/')


@bp.route('/profile')
def user_profile_show():
    if 'user' in session:
        db = DBSession()
        post_list = db.query(Post).filter(Post.user_id == session['id']).all()
        print(session['id'])
        db.close()
        return render_template("profile.html", posts=post_list)
    else:
        print("Once giris yapiniz")
