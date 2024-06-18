#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Config:
    # Flask Configurations
    APP_NAME = 'flask_celery'
    APP_PORT = 5000
    TIMEZONE = 'Asia/Jakarta'

    # MongoDB Configurations
    MONGODB_SETTINGS = {
        "host": "localhost",
        "port": 27017,
        "db": "flask_celery",
        "username": "aselole",
        "password": "secret123",
    }

    # Celery Configurations
    CELERY_BROKER_URL = 'amqp://guest@localhost//'
    RESULT_BACKEND = 'mongodb://aselole:secret123@localhost:27017/flask_celery'
    MONGODB_BACKEND_SETTINGS = {
        'database': 'flask_celery',
        'taskmeta_collection': 'celery_taskmeta'
    }
