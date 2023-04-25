import os
import secrets

from flask import render_template, request, redirect, url_for, flash, session, current_app
from shop import db, app, photos

from .forms import AddProductForm
from .models import Brand, Category, AddProductDB


@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    products = AddProductDB.query.filter(AddProductDB.stock > 0).order_by(
        AddProductDB.id.desc()).paginate(page=page, per_page=8)
    brands = Brand.query.join(AddProductDB, (Brand.id == AddProductDB.brand_id)).all()
    categories = Category.query.join(AddProductDB, (Category.id == AddProductDB.category_id)).all()
    return render_template('products/index.html',
                           products=products,
                           brands=brands,
                           categories=categories)


@app.route('/brands/<int:id>')
def get_brand(id):
    page = request.args.get('page', 1, type=int)
    get_b = Brand.query.filter_by(id=id).first_or_404()
    brand = AddProductDB.query.filter_by(brand=get_b).paginate(page=page, per_page=8)
    brands = Brand.query.join(AddProductDB, (Brand.id == AddProductDB.brand_id)).all()
    categories = Category.query.join(AddProductDB, (Category.id == AddProductDB.category_id)).all()
    return render_template('products/index.html',
                           brand=brand,
                           brands=brands,
                           categories=categories,
                           get_b=get_b)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_product = AddProductDB.query.filter_by(category=get_cat).paginate(page=page, per_page=8)
    brands = Brand.query.join(AddProductDB, (Brand.id == AddProductDB.brand_id)).all()
    categories = Category.query.join(AddProductDB, (Category.id == AddProductDB.category_id)).all()
    return render_template('products/index.html',
                           get_cat_product=get_cat_product,
                           categories=categories,
                           brands=brands,
                           get_cat=get_cat)


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


@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        flash(f'The Brand {brand} has been updated successfully', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html', title='Update Brand Page', updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET', 'POST'])
def deletebrand(id):
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    deletebrand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(deletebrand)
        flash(f'The Brand {deletebrand.name} has been deleted successfully', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f'The Brand {deletebrand.name} cant be deleted', 'warning')
    return redirect(url_for('admin'))


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
        return redirect(url_for('admin'))
    return render_template('products/addbrand.html')


@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecat.name = category
        flash(f'The Category {category} has been updated successfully', 'success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updatebrand.html', title='Update Category Page', updatecat=updatecat)


@app.route('/deletecategory/<int:id>', methods=['GET', 'POST'])
def deletecategory(id):
    if 'email' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('login'))
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(category)
        flash(f'The Category {category.name} has been deleted successfully', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f'The Category {category.name} cant de deleted', 'warning')
    return redirect(url_for('admin'))


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


@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = AddProductDB.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = AddProductForm(request.form)

    if request.method == 'POST':
        product.name = form.name.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.discount = form.discount.data
        product.brand_id = brand
        product.category_id = category
        product.color = form.color.data
        product.description = form.description.data
        for i in range(1, 4):
            image = request.files.get(f'image_{i}')
            if image:
                try:
                    os.unlink(os.path.join(current_app.root_path, f'static/images/{getattr(product, f"image_{i}")}'))
                except Exception as e:
                    print(e)
                setattr(product, f"image_{i}", photos.save(image, name=secrets.token_hex(10) + "."))

        db.session.commit()
        flash(f'The Product {product.name} has been updated successfully', 'success')
        return redirect(url_for('admin'))

    form.name.data = product.name
    form.price.data = product.price
    form.stock.data = product.stock
    form.discount.data = product.discount
    form.color.data = product.color
    form.description.data = product.description

    return render_template('products/updateproduct.html',
                           title='Update Product Page',
                           form=form,
                           brands=brands,
                           categories=categories,
                           product=product)


@app.route('/deleteproduct/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    product = AddProductDB.query.get_or_404(id)
    if request.method == "POST":
        for i in range(1, 4):
            image = request.files.get(f'image_{i}')
            if image:
                try:
                    os.unlink(os.path.join(current_app.root_path, f'static/images/{getattr(product, f"image_{i}")}'))
                except Exception as e:
                    print(e)

        db.session.delete(product)
        db.session.commit()
        flash(f'The Product {product.name} has been deleted successfully', 'success')
        return redirect(url_for('admin'))

    flash(f'The Product {product.name} cant be deleted', 'warning')
    return redirect(url_for('admin'))
