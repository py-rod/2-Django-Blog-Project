## Description

The Django Course Platform is a web application designed to create and manage courses in a blog-style format. It provides essential features like user authentication, user profiles, a search system, and the ability for administrators to create and delete categories and articles.

## Features

- **User Authentication**:
   - User registration: Visitors can create accounts by providing their name, email address, and password.
   - Login: Registered users can log in to their accounts.

- **Password Recovery**:
   - Users can request a password reset if they forget it, receiving a reset link via email.

- **User Profiles**:
   - Each registered user has a customizable profile where they can add additional information, including a profile picture and a brief description.

- **Course Upload (Articles)**:
   - Authenticated users can create, edit, and delete courses, treated as articles in the blog.
   - Courses include titles, descriptions, content, and associated categories.

- **Category Management**:
   - Administrators can create and delete categories to organize the courses.

- **Course Search**:
   - The platform offers a search system, enabling users to find courses by title, description, author, or category.

- **Administrator Access**:
   - Administrators have special permissions to manage categories and courses, including creating and deleting them.



## Create a virtual environment and activate it.

 - python -m venv venv
 - source venv/bin/activate

**Install the project dependencies.**:
 - pip install -r requirements.txt


**Migrate the database.**
 - python manage.py makemigrations
 - python manage.py migrate


**Create a superuser account for admin access.**
 - python manage.py createsuperuser


**Run the development server.**
 - python manage.py runserver
 - Access the application in your browser at http://localhost:8000
