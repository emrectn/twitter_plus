from flask import Blueprint, request, redirect, session
from app.models import Post, DBSession
from time import time


bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/create', methods=['POST'])
def post_create():
    text = request.form.get("text").strip()
    if text:
        if 'user' in session:
            db = DBSession()
            p = Post(text=text, user_id=session['id'], timestamp=int(time()))
            db.add(p)
            db.commit()
            print("-{}- kisisi post atti".format(session['user']))
        else:
            print("-{}- kisisi post atamadi".format(session['user']))

    else:
        print("Gecerli Post girin")
    return redirect('/user/profile')


@bp.route('/show')
def post_show():
    db = DBSession()
    post_list = db.query(Post).filter(Post.user_id == session['id']).all()
    print(post_list)
    return redirect('/user/profile')


@bp.route('/delete', methods=['GET'])
def post_delete():
    post_id = request.args.get('id')
    db = DBSession()
    p = db.query(Post).get(int(post_id))
    if p:
        db.delete(p)
        db.commit()
        print("Post silindi")
    else:
        print("Silinemedi")
        db.close()

    return redirect("/user/profile")
