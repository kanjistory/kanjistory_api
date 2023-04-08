# -*- coding: utf-8 -*-
"""Album model."""

# from http import HTTPStatus
from kanjistory_api.api import db


class Story(db.Model):
    """Story."""
    id = db.Column(db.Integer, primary_key=True)
    kanji = db.Column(db.String(3), nullable=False)
    story = db.Column(db.String(), nullable=False)
