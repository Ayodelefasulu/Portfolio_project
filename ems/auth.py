import functools

from flask import (Blueprint, flash, g, redirect,
    render_template, request, session, url_for)

from werkzeug.security import check_password_hash, generate_password_hash

from ems.dbase import get_db

# Create a Blueprint #then import and register it in the app factory
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        if not firstname:
            error = 'First Name is required.'
        elif not lastname:
            error = 'Last Name is required.'
        elif not email:
            error = 'Email is required.'
        elif not phonenumber:
            error = 'Phone Number is required.'
        elif not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                # Insert into user table
                db.execute(
                    "INSERT INTO user (firstname, lastname, email, phonenumber, username, password) VALUES (?, ?, ?, ?, ?, ?)",
                    (firstname, lastname, email, phonenumber, username, generate_password_hash(password)),
                )
                db.commit()

                # Get the user_id of the newly created user
                user_id = db.execute(
                    "SELECT id FROM user WHERE username = ?",
                    (username,)
                ).fetchone()['id']

                # Insert into profile table
                db.execute(
                    "INSERT INTO profile (user_id, firstname, lastname, email, phonenumber) VALUES (?, ?, ?, ?, ?)",
                    (user_id, firstname, lastname, email, phonenumber),
                )
                db.commit()

            except db.IntegrityError:
                error = "User {} is already registered".format(username)
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username = ?',
                       (username,)).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('dashboard.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
