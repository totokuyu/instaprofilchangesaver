from calistir import calistir
from flask import Flask, render_template, flash, request, url_for, redirect, render_template, request, session, abort
from flask_bootstrap import Bootstrap
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from os import path, environ
import multiprocessing
import time

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Url:', validators=[validators.required()])
    mail = TextField("Email: ", validators=[validators.required()])






@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
       return redirect(url_for("hello"))

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'sifre' and request.form['username'] == 'tolga':
        session['logged_in'] = True

    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()





@app.route("/main", methods=['GET', 'POST'])

def hello():
    form = ReusableForm(request.form)

    print
    form.errors
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']

        if form.validate():
            # Save the comment here.
            if request.form.get('boxtitle') == request.form.get('boxh1') == request.form.get('boxh2')== request.form.get('boxbody') == None:
                flash("En az bir seçim yapmak zorundasınız! ")
            else:
                calistir(name, mail)
                flash('Tarama tamamlandı')


        else:
            flash('Tüm formlar doldurulmalıdır! ')

    return render_template('hello.html', form=form)



if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='127.0.0.3', port=port, debug=True)








