# cart.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from .models import Cart, Product
from . import db
import os
import smtplib
from email.message import EmailMessage

cart = Blueprint('cart', __name__)

@cart.route('/cart')
@login_required
def view_cart():
    lines = Cart.query.filter_by(customer_link=current_user.id).all()
    total_items = sum(l.quantity for l in lines)
    return render_template('cart.html', lines=lines, total_items=total_items)

@cart.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_item(product_id):
    qty = int(request.form.get('quantity', 1))
    if qty < 1:
        qty = 1

    product = Product.query.get_or_404(product_id)
    if product.in_stock <= 0:
        flash('Item is out of stock.', 'error')
        return redirect(url_for('views.shop'))

    existing = Cart.query.filter_by(customer_link=current_user.id,
                                    product_link=product.id).first()
    if existing:
        existing.quantity += qty
    else:
        db.session.add(Cart(quantity=qty, customer_link=current_user.id, product_link=product.id))

    db.session.commit()
    flash('Added to cart.', 'success')
    return redirect(url_for('views.shop'))

@cart.route('/cart/submit', methods=['POST'])
@login_required
def submit_cart():
    lines = Cart.query.filter_by(customer_link=current_user.id).all()
    if not lines:
        flash('Your cart is empty.', 'info')
        return redirect(url_for('cart.view_cart'))

    # Build a simple text summary
    summary_lines = []
    for l in lines:
        summary_lines.append(f"- {l.product.product_name} x {l.quantity}")
    summary_text = "\n".join(summary_lines)

    user_info = f"Customer: {current_user.username} ({getattr(current_user, 'email', 'no-email')})\n"
    body = (
        f"{user_info}"
        f"Submitted cart items:\n\n"
        f"{summary_text}\n\n"
        f"Total items: {sum(l.quantity for l in lines)}\n"
    )

    # Send email
    try:
        send_email(
            subject="Corporate Order Submission",
            body=body,
            to_email=os.environ.get("MANAGER_EMAIL")
        )
    except Exception as e:
        current_app.logger.exception("Failed to send order email")
        flash("Could not submit order (email failed).", "error")
        return redirect(url_for('cart.view_cart'))

    # (Optional) clear the user's cart after sending
    for l in lines:
        db.session.delete(l)
    db.session.commit()

    flash("Order submitted to Corporate.", "success")
    return redirect(url_for('views.shop'))

def send_email(subject: str, body: str, to_email: str):
    """
    Sends a plain-text email using SMTP settings from environment variables.
    Required env vars:
      SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, FROM_EMAIL, MANAGER_EMAIL
    """
    if not to_email:
        raise RuntimeError("MANAGER_EMAIL is not set")

    host = os.environ["SMTP_HOST"]
    port = int(os.environ.get("SMTP_PORT", "465"))
    user = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]
    from_email = os.environ.get("FROM_EMAIL", user)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(body)

    # STARTTLS (port 587). If you use SSL (465), swap to SMTP_SSL and drop starttls().
    with smtplib.SMTP_SSL(host, port) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)

