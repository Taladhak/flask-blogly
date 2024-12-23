"""Blogly application."""

m flask import Flask, render_template, request, redirect
from flask import Flask
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# connect to the database
@app.route('/')
# function redirects to the users page
def root():
    return redirect('/users')

@app.route('/users')
# function displays a page with info on all users
def users_index():
    users= User.query.order_by(User.last_name, User.first_name).all() 
    # return render_template('users/index.html', users=users)
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=["GET"])
# function displays a form to add a new user
def users_new():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
# function displays info on a single user
def users_show(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit')
# function displays a form to edit an existing user
def users_edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
# function edits an existing user
def users_update(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')





connect_db(app)
with app.app_context():
    db.create_all()
