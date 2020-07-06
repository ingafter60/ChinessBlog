## CHINESSBLOG: Build A Blog Based on Chiness Tutorials Using Django 2.2.3

### Step 1: Setup and create django project

	0. Create root dir ChinessBlog & cd ChinessBlog
	1. python -m venv env223
	2. env223\scripts\activate
	3. pip install django==2.2.3
	4. django-admin startproject blogproject .
	5. python manage.py runserver

### Step 2: Create a blog application

	1. python manage.py startapp blog
	2. setting the language and timezone	