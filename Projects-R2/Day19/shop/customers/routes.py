from flask import render_template, request, redirect, url_for, flash
from shop import db, app, bcrypt, login_manager
from flask_login import login_user, logout_user

from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import Register


@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    form = CustomerRegistrationForm()
    if form.validate_on_submit() and request.method == 'POST':
        hash_password = bcrypt.generate_password_hash(form.password.data)
        c_register = Register(name=form.name.data,
                              username=form.username.data,
                              email=form.email.data,
                              password=hash_password,
                              country=form.country.data,
                              city=form.city.data,
                              contact=form.contact.data,
                              address=form.address.data,
                              zipcode=form.zipcode.data)
        print(c_register)
        db.session.add(c_register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('customer/register.html', form=form)


@app.route('/customer/login', methods=['GET', 'POST'])
def customer_login():
    form = CustomerLoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash(f'Welcome {user.name} You are logged in!', 'success')
            return redirect(request.args.get('next') or url_for('home'))
        flash('Wrong password or email', 'danger')
        return redirect(url_for('customer_login'))
    return render_template('customer/login.html', form=form)


@app.route('/customer/logout')
def customer_logout():
    logout_user()
    return redirect(url_for('home'))
