from flask import render_template, request, redirect, url_for, flash, session, current_app
from shop import db, app, photos
from shop.products.models import AddProductDB


def merge_two_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Inputs must be dictionaries")
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


@app.route('/addcart', methods=['POST'])
def add_cart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        product = AddProductDB.query.filter_by(id=product_id).first()

        if product_id and quantity and colors and request.method == 'POST':
            cart_item = {
                product_id: {'name': product.name,
                             'price': product.price,
                             'discount': product.discount,
                             'color': colors,
                             'quantity': quantity,
                             'image': product.image_1}
            }
            if 'shopping_cart' in session:
                if product_id in session['shopping_cart']:
                    flash('This product is already in your shopping cart')
                else:
                    session['shopping_cart'].update(cart_item)
                    return redirect(request.referrer)

            else:
                session['shopping_cart'] = cart_item
                return redirect(request.referrer)
    except KeyError:
        flash('Invalid form data')
    except Exception as e:
        print(e)
        flash('An error occurred while adding the item to the cart')
    return redirect(request.referrer)
