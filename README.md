# Table of Contents

1. [Achievement 1](#achievement-1)
2. [Achievement 2](#achievement-2)

# Achievement 1
1. [Objective](#objective)
2. [Context](#context)
3. [User Goals](#user-goals)
4. [Key Features](#key-features)
5. [Technical Requirements](#technical-requirements)
6. [Brief](#brief)

## Objective
Build the command line version of a Recipe app, which acts as a precursor to its web app counterpart in Achievement 2.

## Context
Building a website with the Django web framework is almost entirely done in Python, and takes advantage of Python’s object-oriented nature. You may also be required to modify the code in the event of any updates to Django—here, it helps to understand the instructions and syntaxes provided. Debugging for errors and exceptions also becomes an easy task with the concepts outlined in this Achievement. This project primarily focuses on learning Python fundamentals, data structures, and object-oriented programming. You'll also learn how to interact with databases using Python, which will help you when you have to do the same with the Django framework. The project also aims to teach you standard programming practices that will make the code simpler easier to read, and robust during execution.

## User Goals
Users should be able to create and modify recipes with ingredients, cooking time, and a difficulty parameter that would be automatically calculated by the app. Users should also be able to search for recipes by their ingredients.

## Key Features
- Create and manage the user’s recipes on a locally hosted MySQL database.
- Option to search for recipes that contain a set of ingredients specified by the user.
- Automatically rate each recipe by their difficulty level.
- Display more details on each recipe if the user prompts it, such as the ingredients, cooking time, and difficulty of the recipe.

## Technical Requirements
- The app should handle any common exceptions or errors that may pop up either during user input, database access, for example, and display user-friendly error messages.
- The app must connect to a MySQL database hosted locally on the system.
- The app must provide an easy-to-use interface, supported by simple forms of input and concise instructions that any user can follow—always assume that they aren’t as technically proficient as you may be. For instance, if the program requires that the user picks an option from a list, instead of having them manually type in the option, list the options with numbers, and have them enter the number corresponding to their choice.
- The app should work on Python 3.6+ installations.
- App code must be well-formatted according to standardized guidelines
- App code should also be supported by concise, helpful comments that illustrate the flow of the program.

## Brief
[Brief](./ach1.pdf)

# Achievement 2
1. [Objective](#objective)
2. [Context](#context)
3. [User_Goals](#user-goals)
4. [Key_Features](#key-features)
5. [Technical_Requirements](#technical-requirements)
6. [Brief](#brief)

## Objective
Take the Recipe app from Achievement 1 and use the Django web framework to develop a fully fledged web application with multiple users and an admin panel.

## Context
This project focuses on creating a web application using the Django framework. To work with Django, you need an understanding of application design patterns and internal language, which you gained in Achievement 1 when using Python to make a command line Recipe app.
Now, in Achievement 2, it’s time for you to rebuild the app using Django Django has the advantage of being neatly moduralized and developer friendly while also being powerful enough to run some of the world’s most popular websites. 
In the project, working with Python-based Django, you’ll develop a full-stack web application using the Django development server. You’ll then deploy the application using Heroku, with a Postgres database at the backend HTML, and CSS-based rendered pages at the frontend and Python-based Django as the web application framework. 
the final web application will be dynamic and multi-user, letting users sign up and create their own content. It’ll also have statistical dashboards, implementing the new data analytics and data visualization skills. Finally, you’ll demonstrate coding best practices by putting the well-tested and well-documented code on GitHub.

## User Goals
Users should be able to create and modify recipes containing ingredients, cooking time, and a difficulty parameter automatically calculated by the application. Users should also be able to search for recipes by ingredient.

## Key Features
- Allow for user authentication, login, and logout.
- Let users search for recipes according to ingredients.
- Automatically rate each recipe by difficulty level.
- Receive user input and handle errors appropriately.
- Display more details on each recipe if the user asks for that.
- Add user recipes to an SQLite database.
- Include a Django Admin dashboard for working with database entries.
- Show statistics and visualizations based on trends and data analysis.

## Technical Requirements
- Works on Python 3.6+ installations and Django version 3.
- Handles exceptions or errors that arise during user input, for example, then displays user-friendly
error messages.
- Connects to a PostgreSQL database hosted locally on the same system (an SQLite database is
needed during the development of your application).
- Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow
instructions. Menus containing features like login and logout must be presented neatly—with
concise and easy-to-follow prompts.
- Code with proper documentation and automated tests is uploaded on GitHub. A
“requirements.txt” file is provided, containing the requisite modules for the project.
- Readme file is provided with instructions on downloading and running the app locally on any
machine

## Brief
[Brief](./ach2.pdf)