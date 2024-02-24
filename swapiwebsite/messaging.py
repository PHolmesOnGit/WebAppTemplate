from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from swapiwebsite.db import get_db

bp = Blueprint('messaging', __name__, url_prefix='/messaging')


@bp.route('/home', methods=('GET', 'POST'))
def home():

    return render_template('messaging/home.html')


@bp.route('/sendmessage', methods=('GET', 'POST'))
def send_message():
    if request.method == 'POST':
        receiver = request.form['receiver']
        message = request.form['message']
        error = None

        if not receiver:
            error = 'Amount is required.'
        elif not message:
            error = 'Message is required.'

        if error is not None:
            flash(error)
        else:
            sender = g.user['username']
            db = get_db()
            db.execute(
                "INSERT INTO messaging (sender, receiver, message) "
                "VALUES (?, ?, ?)",
                (sender, receiver, message),
            )
            db.commit()
            return redirect(url_for("messaging.home"))


    return render_template('messaging/sendmessage.html')


@bp.route('/messagehistory', methods=('GET', 'POST'))
def message_history():

    db = get_db()
    receiver_list = db.execute(
        "SELECT receiver FROM messaging WHERE sender = ?", (g.user['username'],)
    ).fetchall()
    print(receiver_list)

    return render_template('messaging/receiverlist.html', receiver_list=receiver_list)
