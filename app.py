from project import app, db
from flask import render_template, redirect, url_for, flash
from project.forms import LoginForm
from models import UserModel

@app.route('/', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = UserModel.find_by_eid(form.eid.data)
		if user is not None and user.check_password(form.password.data):
			return render_template('base.html')
	return render_template('login.html', form = form)

@app.route('/services')
def services():
	data = UserModel.query.all()
	return render_template('services.html', data=data)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

if __name__ == '__main__':
	app.run(debug = True)