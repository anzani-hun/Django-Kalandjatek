C:\Users\2022404\Desktop\utolso fullstack>python -m venv venv

C:\Users\2022404\Desktop\utolso fullstack>cd venv

C:\Users\2022404\Desktop\utolso fullstack\venv>Scripts\activate

(venv) C:\Users\2022404\Desktop\utolso fullstack\venv>cd..

(venv) C:\Users\2022404\Desktop\utolso fullstack>pip install django

(venv) C:\Users\2022404\Desktop\utolso fullstack>python -m pip install --upgrade pip

(venv) C:\Users\2022404\Desktop\utolso fullstack>pip install djangorestframework

(venv) C:\Users\2022404\Desktop\utolso fullstack>pip freeze

asgiref==3.8.1
Django==5.0.4
djangorestframework==3.15.1
sqlparse==0.5.0
tzdata==2024.1

(venv) C:\Users\2022404\Desktop\utolso fullstack>cd kalandjatek

(venv) C:\Users\2022404\Desktop\utolso fullstack\kalandjatek>django-admin startproject config

(venv) C:\Users\2022404\Desktop\utolso fullstack\kalandjatek>ren config backend

(venv) C:\Users\2022404\Desktop\utolso fullstack\kalandjatek>cd backend

(venv) C:\Users\2022404\Desktop\utolso fullstack\kalandjatek\backend>python manage.py makemigrations

(venv) C:\Users\2022404\Desktop\utolso fullstack\kalandjatek\backend>python manage.py migrate
