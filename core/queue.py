#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celery import Celery
from config import Config

def init_celery():
    celery = Celery('tasks', broker=Config.CELERY_BROKER_URL, backend=Config.RESULT_BACKEND)
    celery.conf.update(
        timezone=Config.TIMEZONE,
        mongodb_backend_settings=Config.MONGODB_BACKEND_SETTINGS,
        broker_connection_retry_on_startup = True
    )

    return celery

celery = init_celery()

@celery.task(name="task_multiply")
def multiply(x, y):
    print("Masuk mas...")
    return x * y
    # raise Exception("This task is designed to fail")
