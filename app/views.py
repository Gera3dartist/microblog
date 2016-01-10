from app.forms import LoginForm
from app.models import User
from flask import render_template, flash, redirect, session, \
    url_for, request, g
from flask.ext.login import login_user, logout_user,\
    current_user, login_required
from app import app, db, lm, oid


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Buddy'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flash('Invalid login')
        return redirect(url_for('/login'))
    # check if user is valid
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        return redirect(url_for('login'))
    remember_me = False
    if remember_me in session:
        remember_me = session.get('remember_me', False)
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    flash('successfully logged in!')
    # TODO: make redirect to edit section
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
