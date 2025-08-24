# CRM_API
CRM API with Custom User model focused on Django Rest Framework


# Git Commands
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main

git pull origin main --allow-unrelated-histories

# Django Commands with Venv
.venv\Scripts\activate
uv pip install django djangorestframework markdown
uv pip install django-filter
cd CRM_API

django-admin startproject CRM-API
django-admin startapp home
python manage.py makemigration
python manage.py makemigrations
python manage.py runserver
python manage.py shell

django-admin --version
doskey /history
