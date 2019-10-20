#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

from datetime import timedelta
from os import environ


class BaseConfig:
	DEBUG = False
	TESTING = False
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_RECORD_QUERIES = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
	JWT_SECRET_KEY = None
	JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=3650)
	FILE_NAME_LENGTH = 32


class DevConfig(BaseConfig):
	DEBUG = True
	TESTING = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
	JWT_SECRET_KEY = 'default-secret'
	DATA_DIR = '.'
	HOST = 'http://localhost:5000/'


class TestConfig(BaseConfig):
	TESTING = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
	JWT_SECRET_KEY = environ.get('SECRET_KEY', 'default-secret')
	DATA_DIR = '.'


class ProdConfig(BaseConfig):
	TESTING = False
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:////db/sqlite3.db'
	JWT_SECRET_KEY = environ.get('SECRET_KEY', None)
	DATA_DIR = environ.get('DATA_DIR', None) or '/data'
	HOST = environ.get('HOST', None)


configs = {
	'development': DevConfig,
	'testing': TestConfig,
	'production': ProdConfig,
	'default': DevConfig
}

