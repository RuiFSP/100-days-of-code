import secrets
import pdfkit
from .. import config

from flask import render_template, request, redirect, url_for, flash, session, make_response
from shop import db, app, bcrypt, login_manager
from flask_login import login_user, logout_user, current_user, login_required

from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import Register, CustomerOrder


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


@app.route('/getorder')
@login_required
def get_order():
    if current_user.is_authenticated:
        customer_id = current_user.id
        invoice = secrets.token_hex(5)
        try:
            order = CustomerOrder(invoice=invoice,
                                  customer_id=customer_id,
                                  orders=session['shopping_cart'])
            db.session.add(order)
            db.session.commit()
            session.pop('shopping_cart', None)  # clear cart afterward
            flash(f'Invoice nº{order.invoice} is successfully created', 'success')
            return redirect(url_for('orders', invoice=invoice))

        except Exception as e:
            print(f'Error {e} occurred')
            flash('something went wrong with order', 'danger')
            return redirect(url_for('get_cart'))


@app.route('/orders/<invoice>')
@login_required
def orders(invoice):
    if current_user.is_authenticated:
        grand_total = 0
        sub_total = 0
        tax = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id).order_by(CustomerOrder.id.desc()).first()
        for _key, product in orders.orders.items():
            discount = (product['discount'] / 100) * float(product['price'])
            sub_total += float(product['price']) * int(product['quantity'])
            sub_total -= discount
            tax = ("%.2f" % (.06 * float(sub_total)))
            grand_total = float("%.2f" % (1.06 * sub_total))
    else:
        return redirect(url_for('customer_login'))
    return render_template('customer/order.html',
                           invoice=invoice,
                           tax=tax,
                           sub_total=sub_total,
                           grand_total=grand_total,
                           customer=customer,
                           orders=orders)


@app.route('/get_pdf/<invoice>', methods=['POST'])
@login_required
def get_pdf(invoice):
    if current_user.is_authenticated:
        grand_total = 0
        sub_total = 0
        tax = 0
        if request.method == 'POST':
            customer_id = current_user.id
            customer = Register.query.filter_by(id=customer_id).first()
            orders = CustomerOrder.query.filter_by(customer_id=customer_id).order_by(CustomerOrder.id.desc()).first()
            for _key, product in orders.orders.items():
                discount = (product['discount'] / 100) * float(product['price'])
                sub_total += float(product['price']) * int(product['quantity'])
                sub_total -= discount
                tax = ("%.2f" % (.06 * float(sub_total)))
                grand_total = float("%.2f" % (1.06 * sub_total))

            rendered = render_template('customer/pdf.html',
                                       invoice=invoice,
                                       tax=tax,
                                       grand_total=grand_total,
                                       customer=customer,
                                       orders=orders)

            pdf = pdfkit.from_string(rendered, False, configuration=config, options={"enable-local-file-access": ""})
            response = make_response(pdf)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attach; filename=' + invoice + '.pdf'
            return response
    return request(url_for('orders', invoice=invoice))
