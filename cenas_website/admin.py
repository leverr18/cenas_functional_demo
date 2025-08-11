from flask import Blueprint, render_template, flash, redirect, url_for, send_from_directory
from flask_login import login_required, current_user
from .forms import ShopItemsForm
from werkzeug.utils import secure_filename
from .models import Product
from . import db
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_FOLDER = os.path.join(os.path.dirname(BASE_DIR), 'media')

os.makedirs(MEDIA_FOLDER, exist_ok=True)

admin = Blueprint('admin', __name__)

@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

@admin.route('/add_items', methods=['GET', 'POST'])
@login_required
def add_items():
    if current_user.id == 1:
        form = ShopItemsForm()

        if form.validate_on_submit():
            product_name = form.product_name.data
            in_stock = form.in_stock.data

            file = form.product_picture.data

            file_name = secure_filename(file.filename)

            file_path = os.path.join(MEDIA_FOLDER, file_name)

            file.save(file_path)

            new_shop_item = Product()
            new_shop_item.product_name = product_name
            new_shop_item.in_stock = in_stock

            new_shop_item.product_picture = file_name

            try:
                db.session.add(new_shop_item)
                db.session.commit()
                flash(f'{product_name} added Successfully', 'success')
                print('Product Added')
                return redirect(url_for('admin.add_items'))
            except Exception as e:
                print(e)
                flash('Product Not Added!!', 'error')

        return render_template('add_shop_items.html', form=form)
    
@admin.route('/shop_items', methods=['GET', 'POST'])
@login_required
def shop_items():
    if current_user.id == 1:
        items = Product.query.order_by(Product.date_added).all()
        return render_template('shop_items.html', items=items)
    else:
        flash("Access Denied", "error")
        return redirect(url_for('views.shop'))
    
    
    

