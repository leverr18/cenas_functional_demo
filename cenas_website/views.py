from flask import Blueprint, render_template, jsonify, request
from cenas_website import dictionaries
from flask_login import login_required
from .models import Product

locations = dictionaries.locations
menu_items = dictionaries.menu_items
weekly_specials = dictionaries.weekly_specials
vegetarian_items = dictionaries.vegetarian_items
drink_items = dictionaries.drink_items

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route("/about-us")
def about_us():
    return render_template("about.html", locations=locations)

@views.route('/locations')
def get_locations():
    return jsonify(locations)

@views.route('/career')
def career():
    return render_template("career.html")

@views.route('/catering')
def catering():
    return render_template("catering.html")

@views.route('/community')
def community():
    return render_template("community.html")

@views.route('/donations')
def donations():
    return render_template("communitydonations.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/weekly_specials_data')
def weekly_specials_data():
    return jsonify(weekly_specials)

@views.route('/menu')
def menu():
    return render_template("menu.html", menu_items=menu_items, weekly_specials=weekly_specials)

@views.route('/menu_data')
def menu_data():
    return jsonify(menu_items)

@views.route('/veggie_menu_data')
def vegetarian_menu_data():
    return jsonify(vegetarian_items)

@views.route('/vegetarian_menu')
def vegetarian_menu():
    return render_template("vegetarian_menu.html", vegetarian_items=vegetarian_items)

@views.route('/gallery')
def gallery():
    return render_template("gallery.html")

@views.route('/drinks')
def drinks():
    return render_template("drinkmenu.html", drink_items=drink_items, weekly_specials=weekly_specials)

@views.route('/drink_data')
def drink_data():
    return jsonify(drink_items)

@views.route('/orderlocation')
def orderlocation():
    return render_template("chooselocation.html", locations=locations)

ROW1 = ["Bar", "Server", "Host & Togo", "Office", "Togo & Catering"]
ROW2 = ["Uniforms", "Foam Cups and Lids", "1-3 Compartment Containers", "Aluminum Foil Pans & Containers", "Portion Cup & Lids", "Plastic & Paper Bags", "Spices", "Cleaning Supplies", "Supplies Available at Corporate"]

@views.route('/shop')
def shop():
    cats_all = ROW1 + ROW2
    # Pull everything at once, then group in Python
    products = Product.query.filter(Product.category.in_(cats_all)).order_by(Product.date_added.desc()).all()
    grouped = {c: [] for c in cats_all}
    for p in products:
        grouped.setdefault(p.category, []).append(p)

    return render_template(
        "shop.html",
        row1=ROW1, row2=ROW2, grouped=grouped
    )

