# ERP-Project-FODS

<p>This is the course project which deals with the construction of erp panel where the student user can register themselves with all the relevant information like Name, Faculty's Name, Courses taken, Credits, Grades and their respective GPA.</p>

## Steps to set up the project:

Steps to setup the project
1. First create a virtual environment with the following set of commands

``` python -m venv env ```

2. To activate the virtual environment, write the following code depending upon the system:
for linux
``` source env/bin/activate ```

for windows
``` env\Scripts\activate.bat ```

3. Clone the ERP Project from the follwoing GitHub Repo
``` git clone https://github.com/RaginBullerpSourceProject.git ```

4. Change the directory to the erp Project using cd command after cloning it
``` cd erpSourceProject ```

5. Install the requirements by the following commands
``` pip install -r requirements.txt ```

6. Now that the server is activated, to run the server type the follwoing
``` python manage.py runserver ```

7. To create superuser type the following
``` python manage.py createsuperuser ```

8. When you make changes to the code such delete, modify etc run the following commands after you're done.
``` python manage.py makemigrations ```
``` python manage.py migrate ```
