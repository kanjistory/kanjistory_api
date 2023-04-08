# -*- coding: utf-8 -*-
"""
    The app module, containing the app factory function.

    isort:skip_file
"""

# For debugging purposes:
import warnings  # noqa
warnings.filterwarnings('error')  # noqa

import sys
import traceback
import warnings
from http import HTTPStatus

from flask import Flask, jsonify
from flask.helpers import get_debug_flag
from werkzeug.exceptions import HTTPException
from sqlalchemy import exc

from .api import api, db
from .story.resources import story_bp


def create_app(config_object=None):
    """ An application factory. """

    app = Flask(__name__.split('.')[0], static_folder='files')

    if config_object is None:
        # pylint: disable=import-outside-toplevel
        if get_debug_flag():
            from kanjistory_api.settings import DevConfig as config_object  # noqa
        else:
            from kanjistory_api.settings import ProdConfig as config_object  # noqa
    app.config.from_object(config_object)

    register_errorhandlers(app)

    api.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.register_blueprint(story_bp)

    return app


# @app.route('/favicon.ico')
#     def favicon():
#         return send_from_directory('client', 'favicon.png', mimetype='image/png')


def register_errorhandlers(app):
    """Register error handlers."""
    # pylint: disable=unused-variable

    def log_exception(exception):
        return api.handle_http_exception(exception)

    app.register_error_handler(HTTPException, log_exception)

    def handle_exception(_, http_error=HTTPStatus.INTERNAL_SERVER_ERROR, msg=None):  # noqa
        if msg is None:
            msg = 'A server error occurred. Please contact support if this persists.'
        exc_info = sys.exc_info()
        exc_str = ''.join(traceback.format_exception(*exc_info))
        if app.config['ENV'] == 'development':
            print(exc_str)
        return jsonify({'message': msg, 'exception': exc_str}), http_error

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return handle_exception(e)

    @app.errorhandler(exc.IntegrityError)
    def handle_exception_integrity_error(e):
        db.session.rollback()
        return handle_exception(e,  HTTPStatus.CONFLICT,
                                'Database error.\nPlease contact support if this error persists.')


if __name__ == '__main__':
    create_app = create_app()
    create_app.run()
else:
    gunicorn_app = create_app()
