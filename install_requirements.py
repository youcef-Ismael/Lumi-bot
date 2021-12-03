import os

os.system('pip install -r requirements.txt')
os.system('python3 manage.py migrate')
os.system('python3 manage.py runserver')
