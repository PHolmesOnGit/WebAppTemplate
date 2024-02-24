
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from swapiwebsite.db import get_db

bp = Blueprint('payments', __name__, url_prefix='/payments')


@bp.route('/home', methods=('GET', 'POST'))
def home():

    return render_template('payments/home.html')


@bp.route('/makepayment', methods=('GET', 'POST'))
def make_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        message = request.form['message']
        error = None


        if not amount:
            error = 'Amount is required.'
        elif not message:
            error = 'Message is required.'

        if error is not None:
            flash(error)
        else:
            username = g.user['username']
            db = get_db()
            db.execute(
                "INSERT INTO payments (username, amount, message) "
                "VALUES (?, ?, ?)",
                (username, amount, message),
            )
            db.commit()
            return redirect(url_for("payments.home"))


    return render_template('payments/makepayment.html')


@bp.route('/paymenthistory', methods=('GET', 'POST'))
def payment_history():

    db = get_db()
    payment_history = db.execute(
        "SELECT * FROM payments WHERE username = ?", (g.user['username'],)
    ).fetchall()

    print(payment_history)

    return render_template('payments/paymenthistory.html', payment_history=payment_history)