from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from swapiwebsite.db import get_db
import datetime
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
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M")
            db = get_db()
            db.execute(
                "INSERT INTO messaging (sender, receiver, message, date, time) "
                "VALUES (?, ?, ?, ?, ?)",
                (sender, receiver, message, date, time),
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
    user_list = []
    for user in receiver_list:
        if user['receiver'] not in user_list:
            user_list.append(user['receiver'])
        else:
            print("User already in list")

    print(user_list)

    return render_template('messaging/receiverlist.html', user_list=user_list)


@bp.route('/messagethread/<string:textee>', methods=('GET', 'POST'))
def message_thread(textee):

    receiver = textee
    db = get_db()
    message_history = db.execute(
        "SELECT * FROM messaging WHERE (sender = ? AND receiver = ?) OR (sender = ? AND receiver = ?)", (g.user['username'], receiver, receiver, g.user['username'])
    ).fetchall()
    print(message_history)

    return render_template('messaging/messagethread.html', message_history=message_history, receiver=receiver)
