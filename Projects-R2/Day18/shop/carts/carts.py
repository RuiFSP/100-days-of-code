import decimal

from flask import render_template, request, redirect, url_for, flash, session, current_app
from shop import db, app, photos
from shop.products.models import AddProductDB
from shop.products.routes import brands, categories
from decimal import Decimal, ROUND_HALF_UP


def merge_two_dicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


@app.route('/addcart', methods=['POST'])
def add_cart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        print(product_id, quantity, colors)
        if product_id and quantity and request.method == 'POST':
            product = AddProductDB.query.filter_by(id=product_id).first()
            colors = product.color.split(',')
            cart_item = {
                product_id: {
                    'name': product.name,
                    'price': product.price,
                    'discount': product.discount,
                    'color': colors[0], # Set the default color to the first color in the list
                    'quantity': quantity,
                    'image': product.image_1,
                    'colors': colors
                }
            }
            print(cart_item)
            if 'shopping_cart' not in session:
                session['shopping_cart'] = cart_item
                flash(f'This product {product.name} was added to your shopping cart', 'success')
            else:
                if product_id in session['shopping_cart']:
                    item = session['shopping_cart'][product_id]
                    item['quantity'] = int(item['quantity']) + int(quantity)
                    session.modified = True
                    flash(f'This product {product.name} is already in your shopping cart', 'warning')
                else:
                    session['shopping_cart'].update(cart_item)
                    flash(f'This product {product.name} was added to your shopping cart', 'success')

            return redirect(request.referrer)

    except Exception as e:
        print(e)
        flash('This product cannot be added to cart', 'danger')

    return redirect(request.referrer)



@app.route('/carts')
def get_cart():
    shopping_cart = session.get('shopping_cart', {})
    if not shopping_cart or len(shopping_cart) <= 0:
        return redirect(url_for('home'))

    subtotal = Decimal('0')
    discount = Decimal('0')
    for product in shopping_cart.values():
        discount += Decimal(str(product['discount'])) / Decimal('100') * Decimal(str(product['price'])) * Decimal(
            str(product['quantity']))
        subtotal += Decimal(str(product['price'])) * Decimal(str(product['quantity']))
    subtotal -= discount
    tax = Decimal('.06') * subtotal
    grand_total = subtotal + tax

    with decimal.localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        subtotal = subtotal.quantize(Decimal('.01'))
        discount = discount.quantize(Decimal('.01'))
        tax = tax.quantize(Decimal('.01'))
        grand_total = grand_total.quantize(Decimal('.01'))

    return render_template('products/carts.html',
                           products=shopping_cart,
                           subtotal=subtotal,
                           discount=discount,
                           tax=tax,
                           grand_total=grand_total,
                           brands=brands(),
                           categories=categories())


@app.route('/updatecart/<int:id>', methods=['POST'])
def update_cart(id):
    if 'shopping_cart' not in session and len(session['shopping_cart']) <= 0:
        return redirect(url_for('home'))
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        color = request.form.get('colors')
        try:
            session.modified = True
            for key, item in session['shopping_cart'].items():
                if int(key) == id:
                    item['quantity'] = quantity
                    item['color'] = color
                    print(item)
                    flash('Item updated successfully', 'success')
                    return redirect(url_for('get_cart'))
        except Exception as e:
            print(e)
            flash('Item update failed', 'danger')
            return redirect(url_for('get_cart'))


@app.route('/deleteitem/<int:id>')
def delete_item(id):
    if 'shopping_cart' not in session and len(session['shopping_cart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key, item in session['shopping_cart'].items():
            if int(key) == id:
                session['shopping_cart'].pop(key, None)
                flash('Item removed successfully', 'success')
                return redirect(url_for('get_cart'))
    except Exception as e:
        print(e)
        flash('Item removal failed', 'danger')
        return redirect(url_for('get_cart'))


@app.route('/clearcart')
def clear_cart():
    try:
        session.pop('shopping_cart', None)
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        return redirect(url_for('home'))
