# Backend Setup for ToDo List App
This repository contains the backend for the Todo List application. 
Follow the steps below to set up and run the application.

## Prerequisites
Make sure you have the following installed:

- Python 3.x
- pip (Python package manager)
- virtualenv (for creating isolated environments)

## Create and Activate Virtual Environment
- python3 -m venv backendvenv
- source backendvenv/bin/activate

##  Install Required Packages
- pip install -r requirements.txt
- To update requirements file, run this command with approriate path:
- `/home/giang/projects/ToDoList-DjangoReact/backend/backendvenv/bin/pip freeze > requirements.txt`

# Later we'll run migrations with:
  - python manage.py makemigrations 
  - python manage.py migrate

# And create a superuser with:
  - python manage.py createsuperuser

## Deactivate
- deactivate