# RP-protfolio tutorial "https://realpython.com/get-started-with-django-1/"

## Project Overview
    This is my first Django project!

## Specification
    Runs on Python 3.11 and HTML5 with dependencies

## Project Setup
    Follow these steps to set up the project

1. Install Python 3.11 or later

2. Set Up the Development Environment

    ```bash
    mkdir rp-portfolio
    ```

 3. Go to your directory   
    
    ```bash
    cd rp-portfolio
    ```

4. create a virtual environment

    ```bash
    python -m venv venv
    ```

5. activate the virtual environment 

    ```bash
    .\venv\Scripts\activate
    ```

6. install Django

    ```bash
    python -m pip install Django
    ```

7. create the project

    ```bash
    django-admin startproject p_portfolio . # Don’t forget to add the dot (.) 
    ```

8. run the project

    ```bash
    python manage.py runserver
    ```

9. Create an app named MyProtfolio

    ```bash
    python manage.py startapp MyProtfolio
    ```

10. Create a View

    ```
    view function named home()
    ```

11. Create the HTML template to display to the user

12. Create the template/ directory, a subdirectory named pages/, and subsequently a file named home.html inside it

    ```
    mkdir -p MyProtfolio/templates/MyProtfolio
    MyProtfolio/templates/MyProtfolio/home.html
    ```

14. Add a Route
    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("pages.urls")),
    ]
    ```

15. Create MyProtfolio/urls.py

    ```
    from django.urls import path
    from pages import views

    urlpatterns = [
        path("", views.home, name='home'),
    ]
    ```

14. python manage.py runserver

15. Add Bootstrap to Your App (add an external CSS) (One of the most popular CSS frameworks is Bootstrap)

    Create a directory named templates/ in the rp-portfolio/ folder
    templates/base.html

    "DIRS": [
            BASE_DIR / "templates/",
        ],

16. Add the Projects App

    ```
    python manage.py startapp projects
    ```

17. Define a Model (a built-in object relational mapper (ORM)) 
    An ORM is a program that allows you to create classes that correspond to database tables

    The model that you’ll create will be named Project and will have the following fields:

    Name	         Description
    title	         A short string field to hold the name of your project
    description	     A larger string field to hold a longer piece of text
    technology	     A string field, but its contents will be limited to a select number of choices

18. Create a migration

    ```
    python manage.py makemigrations projects
    ```

19. Apply the migrations

    ```
    python manage.py migrate projects
    ```

20. Dive Into the Django Shell

    ```
    python manage.py shell
    ```

21. Create an instance of the Project class

    >>> first_project = Project(
    ...     title="My First Project",
    ...     description="A web development project.",
    ...     technology="Django",
    ... )
    >>> first_project.save()

22. Go on and create two additional projects in the database:

    >>> second_project = Project(
    ...     title="My Second Project",
    ...     description="Another web development project.",
    ...     technology="Flask",
    ... )
    >>> second_project.save()

    >>> third_project = Project(
    ...     title="My Third Project",
    ...     description="A final development project.",
    ...     technology="Django",
    ... )
    >>> third_project.save()
    >>> exit()

23. Create the Views
        
        In the projects app, you’ll create two different views:

            1. An index view that shows a snippet of information about each project
            2. A detail view that shows more information on a particular topic

        You’ll add both views to the views.py file that Django already created for you. 
        Inside views.py, you’ll need to import the Project class from models.py and create a project_index() function 
        that renders a template named project_index.html. In the body of this function, 
        you’ll make a Django ORM query to select all the objects in the Project table:

24. Craft the Templates

    ```
    mkdir -p projects/templates/projects
    projects/templates/projects/project_index.html
    projects/templates/projects/project_detail.html
    ```

25. Add the Routes 
    
    creating a projects/urls.py

26. Leverage the Django Admin Site

    ```
    python manage.py migrate
    ```

27. Access the Django admin site

    ```
    python manage.py createsuperuser
    ```

28. Upload Images
29. Create a new migration and then migrate the changes

    ```
    (venv) $ python manage.py makemigrations projects
    Migrations for 'projects':
        projects/migrations/0002_project_image.py
            - Add field image to project

    (venv) $ python manage.py migrate projects
        Operations to perform:
            Apply all migrations: projects
        Running migrations:
            Applying projects.0002_project_image... OK
    ```