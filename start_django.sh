#!/bin/bash
cd lumi-bot/lumi-frontend
ng build --output-path ../lumi_backend/static/angular --output-hashing none
cd ../lumi_backend
python3 manage.py runserver
