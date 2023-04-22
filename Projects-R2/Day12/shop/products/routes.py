from flask import render_template, request, redirect, url_for, flash, session
from shop import db, app, photos
from .models import Brand, Category, AddProductDB
from .forms import AddProductForm
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} has been added successfully', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'The Category {getcat} has been added successfully', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProductForm(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        stock = form.stock.data
        discount = form.discount.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        color = form.color.data
        description = form.description.data
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        add_product = AddProductDB(name=name,
                                   price=price,
                                   discount=discount,
                                   stock=stock,
                                   color=color,
                                   description=description,
                                   brand_id=brand,
                                   category_id=category,
                                   image_1=image_1,
                                   image_2=image_2,
                                   image_3=image_3)

        db.session.add(add_product)
        flash(f'The Product {name} has been added successfully', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', title='Add Product Page', form=form, brands=brands,
                           categories=categories)
