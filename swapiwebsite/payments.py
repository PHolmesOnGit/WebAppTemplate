
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from swapiwebsite.db import get_db

bp = Blueprint('payments', __name__, url_prefix='/payments')


@bp.route('/home', methods=('GET', 'POST'))
def home():

    return render_template('payments/home.html')
