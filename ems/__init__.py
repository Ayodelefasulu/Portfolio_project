""" This is the application factory where the major engine resides """

import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ems.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html')

    # database configurations and definitions are register here
    from . import dbase
    dbase.init_app(app)

    # this is the authentication blueprint being register here
    from . import auth
    app.register_blueprint(auth.bp)

    # blueprint for the dashboard registered here
    from . import dashboard
    app.register_blueprint(dashboard.bp)
    app.add_url_rule('/dashboard', endpoint='dashboard_index')

    # profile blueprint being registered here
    from . import profile
    app.register_blueprint(profile.bp)

    return app
