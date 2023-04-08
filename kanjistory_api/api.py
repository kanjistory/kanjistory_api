"""Api extension initialization"""

from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

api = Api(
    # authorizations=authorizations,
    # security='access_token'
)

db = SQLAlchemy()
