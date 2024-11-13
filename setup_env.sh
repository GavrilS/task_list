#!/bin/bash

python3 -m venv env
source env/bin/activate
python3 -m pip install Flask
python3 -m pip freeze > requirements.txt
deactivate
