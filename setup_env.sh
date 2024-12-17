#!/bin/bash

rm -rf env/
python3 -m venv env
source env/bin/activate
# python3 -m pip install Flask SQLAlchemy mysql-connector-python
# python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
deactivate
