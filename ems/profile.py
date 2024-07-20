""" This is profile blueprint """

from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from ems.auth import login_required
from ems.dbase import get_db

# create blueprint
bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    # Your settings view logic here
    return render_template(url_for(profile/settings.html))

