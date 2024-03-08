from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import requests
import random
from swapiwebsite.auth import login_required

bp = Blueprint('home', __name__)

@bp.route('/' , methods=('GET', 'POST'))
@login_required
def index():

    return render_template('homepage/index.html')
