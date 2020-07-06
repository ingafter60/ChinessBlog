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
	2. register the blog app
	3. setting the language and timezone	

### Step 3: Create a database model for Django blogs

	1. Create model Category
	2. Create model Tag
	3. Create model Post with its relationship with Category(One-To-Many) and Tag(Many-To-Many)	

### Step 4: Django migration, migrate and operation database

	1. python manage.py makemigration
	2. python manage.py migrate
	3. python manage.py createsuperuser
	4. register models to admin
	5. run server
	6. Add some categories, tags, and posts

### Step 5.1: blog index view (hellow world)

	1. Create blog/urls.py
	2. Use views.index path to connect index fucntion in views
	3. Write view function for index
	4. Configure project URL
