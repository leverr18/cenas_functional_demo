# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf.file import FileField, FileRequired

# === Categories (value, label) ===
CATEGORIES = [
    ("Bar", "Bar"),
    ("Server", "Server"),
    ("Host & Togo", "Host & Togo"),
    ("Office", "Office"),
    ("Uniforms", "Uniforms"),
    ("Togo & Catering", "Togo & Catering"),
    ("Foam Cups and Lids", "Foam Cups and Lids"),
    ("1-3 Compartment Containers", "1-3 Compartment Containers"),
    ("Aluminum Foil Pans & Containers", "Aluminum Foil Pans & Containers"),
    ("Portion Cup & Lids", "Portion Cup & Lids"),
    ("Plastic & Paper Bags", "Plastic & Paper Bags"),
    ("Spices", "Spices"),
    ("Cleaning Supplies", "Cleaning Supplies"),
    ("Supplies Available at Corporate", "Supplies Available at Corporate"),
]

# ===== Auth forms (unchanged except Length capitalization) =====
class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    password1 = PasswordField('Enter your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm your Password', validators=[DataRequired(), Length(min=6)])
    registration_code = StringField('Employee Registration Code', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Enter your Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password')

# ===== Shop forms =====
class ShopItemsForm(FlaskForm):
    product_name = StringField('Name of Product', validators=[DataRequired()])
    in_stock = IntegerField('In Stock', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField('Product Picture', validators=[FileRequired()])
    category = SelectField("Category", choices=CATEGORIES, validators=[DataRequired()])
    add_product = SubmitField('Add Product')

class ProductEditForm(FlaskForm):
    product_name = StringField("Product Name", validators=[DataRequired()])
    in_stock = IntegerField("In Stock", validators=[DataRequired(), NumberRange(min=0)])
    # Optional: only replace if a new file is uploaded
    product_picture = FileField("Replace Picture (optional)", validators=[Optional()])
    category = SelectField("Category", choices=CATEGORIES, validators=[DataRequired()])
    save = SubmitField("Save Changes")



