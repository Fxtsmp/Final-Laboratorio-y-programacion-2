#!/usr/bin/env bash

cd flask_venv
cd bin
source activate
cd ..
cd ..
export FLASK_APP=$1
export FLASK_ENV=development
flask run
