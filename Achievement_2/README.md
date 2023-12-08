# Table of Contents

# Achievement 2

1. [Exercise 1](#exercise-1)
2. [Exercise 2](#exercise-2)
3. [Exercise 3](#exercise-3)
4. [Exercise 4](#exercise-4)
5. [Exercise 5](#exercise-5)

# Exercise 1

## Table of Contents

1. [Check Python Version](#check-python-version)
2. [Set Up a Virtual Environment](#set-up-a-virtual-environment)
3. [Install Django](#install-django)

## Check Python Version

Run command python3 -V to check for version 3.8.0

![Step_1](./exercise_2.1/step1.png)

## Set Up a Virtual Environment

Create a new virtualenvironment called achievement2-practice. Confirm it's active in the terminal.

![Step_2](./exercise_2.1/step2.png)

## Install Django

While in virtual environment achievement1-practice, pip install django and check version after install.

![Step_3](./exercise_2.1/step3.png)

# Exercise 2

1. [Create A2_Recipe_App Folder](#create-a2_recipe_app-folder)
2. [Create a2-ve-recipeapp Virtual Environment](#Create-a2-ve-recipeapp-virtual-environment)
3. [Install Django in Virtual Environment](#install-django-in-virtual-environment)
4. [Create Django Project Named recipe_project](#create-django-project-named-recipe_project)
5. [Rename recipe_project Project Directory src](#rename-recipe_project-project-directory-src)
6. [Run Migrations and Run Rerver](#run-migrations-and-run-sever)
7. [Create SuperUser and Sign In](#create-superuser-and-sign-in)

## Create A2_Recipe_App Folder

![Step_1](exercise_2.2/screenshots/step1.png)

## Create a2-ve-recipeapp Virtual Environment

![Step_2](exercise_2.2/screenshots/step2.png)

## Install Django in Virtual Environment

![Step_3](exercise_2.2/screenshots/step3.png)

## Create Django Project Named recipe_project

![Step_4](exercise_2.2/screenshots/proj_contents_before_renaming.jpg)

## Rename recipe_project Project Directory src

![Step_5](exercise_2.2/screenshots/proj_contents_after_renaming.jpg)

## Run Migrations and Run Rerver

![Step_6_1](exercise_2.2/screenshots/step6p1.png)
![Step_6_2](exercise_2.2/screenshots/step6p2.png)

## Create SuperUser and Sign In

![Step7](exercise_2.2/screenshots/admin-dashboard.jpg)

# Exercise 3

## Table of Contents

1. [Create App Schema](#create-app-schema)
2. [Establish Project Structure](#establish-project-structure)
3. [Migrate Models](#migrate-models)
4. [Test Models](#test-models)

## Create App Schema

Identify the desired attributes of each entity and their relation with other entities.

![Step_1](./exercise_2.3/screenshots/schema.jpg)

## Establish Project Structure

Create the apps drawn out in the schema and include links to projects in settings.py

![Step_2](./exercise_2.3/screenshots/project-structure.jpg)

## Migrate Models

After building models within each app, register the models in their respective admin.py, then migrate.

![Step_3](./exercise_2.3/screenshots/run-migrations.jpg)

## Test Models

Build tests for all apps, respectively; run tests.

![Step_4](./exercise_2.3/screenshots/Test-Report.jpg)

# Exercise 4

## Table of Contents

1. [Create Welcome Page](#creat-welcome-page)

## Create Welcome Page

Modify URLs to send user a welcome page with a basic outline.

![Step_1](./exercise_2.4/src/screenshots/welcome.jpg)

# Exercise 5

## Table of Contents

1. [Update Models](#update-models)
2. [Add Records](#add-records)
3. [Welcome Page](#welcome-page)
4. [Recipe Details](#recipe-details)
5. [Test](#test)

## Update Models

Update neccessary models.py to facilitate url paths.
Update neccessary url.py for path logic.
Update neccessary views.py for path and view logic.

makemigrations, migrate, runserver

## Add Records

Download food images to a new media/recipes directory.
Go into admin panel to update recipes with corresponding images.

## Welcome Page

Create Static directory, set up static routing is settings.py.

Update welcome page for better UI/UX, add a button to route to recipe list view with recipes_list.html template.

## Recipe Details

Create recipes_details.html to display recipe details.

## Test

Test all links and ensure they pass.
