# -*- coding: utf-8 -*-
"""Application configuration."""
import datetime
import os


class Config:
    """Base configuration."""

    SECRET_KEY = os.environ.get("SECRET", "flask-unicorn-rainbows-secret-key")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_TITLE = "Test API"
    API_VERSION = "0.1.0"
    OPENAPI_VERSION = "3.0.3"
    SWAGGER_UI_LANGUAGES = ["en"]
    SWAGGER_VALIDATOR_URL = ""
    SWAGGER_UI_OAUTH_CLIENT_ID = None
    SWAGGER_UI_JSONEDITOR = True

    MYSQL_DATABASE_CHARSET = "utf8mb4"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite://")


class ProdConfig(Config):
    """Production configuration."""

    ENV = "production"


class DevConfig(Config):
    """Development configuration."""

    ENV = "development"

    OPENAPI_JSON_PATH = "openapi.json"
    OPENAPI_URL_PREFIX = "/docs"
    OPENAPI_REDOC_PATH = "/redoc/"
    OPENAPI_REDOC_URL = ("https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js")
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_SWAGGER_UI_VERSION = "3.18.3"

    SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI.replace("%p", Config.PROJECT_ROOT)


class TestConfig(Config):
    """Test configuration."""

    ENV = "test"

    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI", "sqlite://")  # defaults to in-memory DB
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("%p", Config.PROJECT_ROOT)
    SQLALCHEMY_DATABASE_URI += "&local_infile=1"
    PRESERVE_CONTEXT_ON_EXCEPTION = False  # prevents double error when assert fails
