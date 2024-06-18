#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify, request
from core.app import init
from core.queue import multiply

app = init()

@app.route('/')
def index():
    return jsonify(message="Welcome to the Flask + Celery app")

@app.route('/multiply', methods=['POST'])
def task_multiply():
    try:
      # Extract data from JSON request
        data = request.json
        x = data['x']
        y = data['y']
      
        # Call the 'multiply' task asynchronously and get the result object
        result = multiply.delay(x, y)
        return jsonify(task_id=result.id)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=app.config.get("APP_PORT", 5000),
        debug=True
      )
