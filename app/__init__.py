from flask import Flask, render_template, request, redirect
# Flas modülümüzü app ile kullanmamızı sağlıyor
app = Flask(__name__)
isim = 'emre'
posts = []


@app.route('/', methods=['GET'])
def post_at():
    return render_template("index.html", post_list=posts)


@app.route('/create', methods=['POST'])
def create_post():
    p = request.form.get("text")
    if p.strip():
        posts.append(p)
    return redirect('/')
