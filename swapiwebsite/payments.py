
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from swapiwebsite.db import get_db

bp = Blueprint('payments', __name__, url_prefix='/payments')


@bp.route('/home', methods=('GET', 'POST'))
def home():

    return render_template('payments/home.html')


@bp.route('/makepayment', methods=('GET', 'POST'))
def makepayment():
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
            db = get_db()
            db.execute(
                "INSERT INTO payments (amount, message) "
                "VALUES (?, ?)",
                (amount, message),
            )
            db.commit()
            return redirect(url_for("payments.home"))


    return render_template('payments/makepayment.html')


@bp.route('/paymenthistory', methods=('GET', 'POST'))
def paymenthistory():

    return render_template('payments/paymenthistory.html')