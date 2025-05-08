from ctypes import resize
from app import myapp_obj
from flask import Flask, request, redirect, request, render_template, flash, url_for
from flask_sqlalchemy import SQLAlchemy # Added SQLAlchemy
from app.forms import RecipeForm, RegistrationForm, LoginForm # importing from forms.py
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from app.models import Recipe, User # importing from models.py
from app import db
from datetime import datetime # added datetime
# from <X> import <Y>

'''
Setup instructions:

Clone repo
Navigate to folder

run: 
python3 -m venv venv
source venv/bin/activate

install necessary libraries using pip3

run in terminal:
flask shell
from app import db
db.create.all()
exit()

python3 run.py

run in terminal to stop virtual environment:

deactivate

'''

@myapp_obj.route("/") # http://127.0.0.1:5000/
def main():
    return redirect(url_for("login"))

@myapp_obj.route("/recipes")
def show_all_recipes():
    recipe = Recipe.query.all() # get all recipes
    return redirect("hello.html", recipe=recipe)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST']) # http://127.0.0.1:5000/recipe/new
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        #create recipe
        new_recipe = Recipe(title=form.title.data, description=form.description.data, ingredients=form.ingredients.data, instructions=form.instructions.data, date=datetime.now())
        db.session.add(new_recipe) #adding to database
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("new.html", form=form) #recipe form

@myapp_obj.route("/recipe/<int:integer>") # http://127.0.0.1:5000/recipe/<enter number here>
def return_recipe(integer):
    recipe = Recipe.query.get(integer) # get recipe number
    if recipe is None:
        print("Recipe not found") #prints to terminal
        return ""
    return render_template("return_rec.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:integer>/delete") # http://127.0.0.1:5000/recipe/<enter number here>/delete
def delete_recipe(integer):
    del_rec = Recipe.query.get(integer) # get recipe number
    db.session.delete(del_rec) #delete
    db.session.commit()

    return f"Recipe deleted: {integer}"

@myapp_obj.route("/registration", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data #1
        email = form.email.data
        password = form.password.data #1
        users = User.query.all()
        if email in users:
            flash("Email is taken.")
        else:
            u = User(username=username, email=email, password=password) #1
            db.session.add(u)#1
            db.session.commit() #1
            print(f"User registered: {username}")
        return redirect("/")
    return render_template("registration.html", form=form)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and  user.password == password:
            login_user(user)
            flash('Logged in successfully.')
            print("Logged in successfully.")
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('protected'))
        else:
            print("Failed to login")
            flash('Invalid username or password.')
    return render_template("login.html", form=form)

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully')
    return redirect(url_for('main'))    

@myapp_obj.route('/protected')
@login_required
def protected():
    return render_template("protected.html")
        
