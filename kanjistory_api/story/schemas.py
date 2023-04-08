# -*- coding: utf-8 -*-
"""
Schema used by REST interface.
"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Story


class StorySchema(SQLAlchemyAutoSchema):
    """Story schema."""
    class Meta:
        """Meta class."""
        model = Story
        load_instance = True
        include_fk = True
        dump_only = ('id',)
