from flask import Flask, render_template, request, redirect, session
from time import time
from datetime import datetime


app = Flask(__name__)
posts = []
users = {}
users['a'] = {'name': 'a', 'surname': 'a', 'password': 'a'}


app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


@app.route('/')
def kayit_yap():
    return render_template("singin.html")


@app.template_filter('datetimefilter')
def utctodatetime(v):
    return str(datetime.fromtimestamp(v))[:-7]


@app.route("/index", methods=['GET'])
def post_yonlendir():
    return render_template("index.html", post=posts, user=users)


@app.route("/create", methods=['POST'])
def post_yazdir():
    text = request.form.get("text")
    current_time = time()
    if 'user' in session:
        p = {'text': text, 'time': current_time, 'user': session['user']}
        if p['text'].strip():
            posts.append(p)
            print("Twitt :  "+session['user'])

        return redirect("/index")
    else:
        return redirect("/give_info?info=Once Giris Yapiniz")


@app.route('/delete', methods=['GET'])
def delete_post():
    index = int(request.args.get("id"))
    posts.pop(index-1)
    return redirect('/index')


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


@app.route("/add_user", methods=['POST'])
def new_user():
    name = request.form.get("name")
    surname = request.form.get("surname")
    password = request.form.get("password")
    email = request.form.get("email")
    if email not in users and name != 'ülkü':
        users[email] = {'name': name, 'surname': surname, 'password': password}
        print("{} kisisi kayit oldu".format(name))
        message = "Basariyla kayit oldunuz. Lütfen Giris Yapiniz"

    else:
        message = "Bu email zaten var"
        print(message)
    return redirect("/give_info?info="+message)


@app.route("/sign_in", methods=['POST'])
def sign_in():
    email = request.form.get("id")
    print(email)
    password = request.form.get("password")
    print(password)
    if email in users:
        if users[email]['password'] == password:
            session['user'] = email
            print("{} Kisisi oturum acti".format(session['user']))
            return redirect("/index")
        else:
            message = "Yanlis kullanici sifresi"
            print(message)
    else:
        message = "Böyle bir kayit bulunamadi"
        print(message)

    return redirect("/give_info?info="+message)

# @app.route("/logout/<str:email>") parametre yollamak istenirse
# def logout(email):parametre


@app.route("/logout")
def logout():
    if 'user' in session:
        print("{} cikis yapti".format(session['user']))
        del session['user']
        message = "Cikis Yapildi"
    else:
        message = "Once giris yapiniz"
    return redirect("/give_info?info="+message)


@app.route("/give_info")
def giveinfo():
    message = request.args.get("info")
    print(message)
    return render_template("/info.html", message=message)
