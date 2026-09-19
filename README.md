# Resume Web App

A simple Django web application that displays a resume using data passed from a Python view to an HTML template.

## Project Summary

### Approach

I created a Django project and a resume app. The resume details were stored in a Python dictionary inside the view and passed to the HTML template as context.

I configured URL routing to connect the project with the resume app. A base template was created using `{% extends %}`, and the resume details were displayed using Django template variables.

I used `{% for %}` to display skills and education, `{% if %}` to display a gender-specific emoji, and `{% static %}` to connect the CSS file.

### Challenges

The main challenge was understanding how data is passed from the Django view to the template. I also learned how to loop through lists and dictionaries using Django template tags and how template inheritance works.

### Learning Outcomes

This project helped me understand the basic Django workflow, including:

* Creating a Django project and app
* URL routing
* Creating views
* Passing context data to templates
* Using Django template tags
* Using static CSS files
* Conditional rendering and loops

Overall, the project gave me practical experience in building a simple dynamic web page using Django.

## Technologies Used

* Python
* Django
* HTML
* CSS
* Django Template Language
