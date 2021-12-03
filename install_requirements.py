import os

os.system('pip install -r requirements.txt')
os.system('py manage.py migrate')
os.system('py manage.py runserver')