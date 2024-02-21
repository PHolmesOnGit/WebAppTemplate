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

    def get_character():
        # calls the swapi api to get a random character
        # returns the character data
        # 17 in the Swapi api returns a 404 error. We work around that by using the try statement
        random_num = random.randint(1, 82)
        print(random_num)
        url = "https://swapi.dev/api/people/" + str(random_num) + "/"
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return get_character()
        data = response.json()
        return data

    return render_template('homepage/index.html', data=get_character())
