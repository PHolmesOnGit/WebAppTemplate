from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from swapiwebsite.auth import login_required
from swapiwebsite.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():

    return render_template('homepage/index.html')