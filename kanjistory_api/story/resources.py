# -*- coding: utf-8 -*-
"""
Album API endpoints.
"""

from flask_smorest_sqla import CRUDBlueprint

from kanjistory_api.api import db

from .models import Story
from .schemas import StorySchema

story_bp = CRUDBlueprint(
    'Stories',
    __name__,
    url_prefix='/story',
    model_class=Story,
    schema_class=StorySchema,
    db=db,
    description='Story CRUD operations'
)
