#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mongoengine 
from flask import Flask
from config import Config

def init():
    app = Flask(__name__)
    app.config.from_object(Config)

    configure_db(app.config.get("MONGODB_SETTINGS", {}))
    return app

def configure_db(config):
    client = mongoengine.connect(
        db=config.get("db"), 
        host=config.get("host"), 
        port=int(config.get("port")),
        username=config.get("username"),
        password=config.get("password")
    )

    try:
        print(f"Ping Database: {client.admin.command('ping')}")
    except Exception as e:
        print(f"Error Connecting to database: {e}")

    return client
