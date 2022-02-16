# Application Factory
# The __init__.py serves double duty:
# it will contain the application factory,
# and it tells Python that the rest_web
# directory should be treated as a package.

from flask import Flask
from os import makedirs, path
from .rest.rest import rest_api
from .site.site import web_site
from .db import init_app
from .login.login import log_user

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='secret',
        DATABASE=path.join(app.instance_path, 'movies_site.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(rest_api)
    app.register_blueprint(web_site)
    # need to register a route for test de db

    # register db in the app
    init_app(app)
    app.register_blueprint(log_user)
    return app
