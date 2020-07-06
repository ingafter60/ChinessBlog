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

### Step 5.2: blog index view 

	1. Use django template system
	2. Create: md templates\blog
	3. Create: touch templates\blog\index.html
	4. Add codes to index.html

	NOTE:
	Here we are no longer directly to the string passed HttpResponse, but to call django provided renderfunctions. This function is constructed based on the parameters we pass in HttpResponse.

	We first pass the HTTP request into it, then renderfind the blog template file based on the value of the second parameter / index.html and read the contents of the template. After renderour passed contextthe value of the template parameter variables replace the value of the variable we pass, {{ title }}is replaced by contextthe dictionary titlecorresponding to the value, empathy {{ welcome }}also be replaced by the corresponding value.

	Eventually, the contents of the string our HTML template is passed to the HttpResponseobject and return to the browser (django at rendera function in implicitly to help us complete this process), it showed us to write HTML on this user's browser The content of the template.	

