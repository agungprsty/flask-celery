## Basic REST API with Flask, Celery, RabbitMQ and MongoDB

### Prerequisite

1. Python 3.x
2. Docker
3. Docker Compose

### How to use

1. Clone this project and go to working directory
2. Create virtual env:
   ```bash
   $ python3 -m venv venv
   ```
3. Install the required dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```
4. Rename `config.py.example` to `config.py` and adjust accordingly
5. Running service docker:
    ```bash
    $ docker compose up -d
    ```
6. Running Application Flask:
    ```bash
    $ python3 -m main
    ```
7. Running Celery worker:
    ```bash
    $ celery -A core.queue worker --loglevel=info
    ```
8. Check endpoint:
    - GET: http://127.0.0.1:5000/
    - POST: http://127.0.0.1:5000/multiply
9. and enjoy this exploration!

### Create new issue if you need help :)