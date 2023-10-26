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

## Images

![111](https://github.com/py-rod/Django-Blog-Project/assets/103091079/af135c50-29d5-4af5-b3f0-33086683cc7e)

![22](https://github.com/py-rod/Django-Blog-Project/assets/103091079/25bf60d8-c315-40c3-a27d-0400518b9fae)

![33](https://github.com/py-rod/Django-Blog-Project/assets/103091079/c256b941-22c3-4e61-b90a-4989a7b37fce)

![44](https://github.com/py-rod/Django-Blog-Project/assets/103091079/cb88f901-5048-4839-b653-88f127f016ee)

![66](https://github.com/py-rod/Django-Blog-Project/assets/103091079/02e22722-f1e1-4203-b954-7c76548bc628)

![777](https://github.com/py-rod/Django-Blog-Project/assets/103091079/94fa5693-7afb-4701-bf4d-66dfd5ed081a)

![88](https://github.com/py-rod/Django-Blog-Project/assets/103091079/975c6a14-5fdc-4f85-8c7d-963722068d6d)







