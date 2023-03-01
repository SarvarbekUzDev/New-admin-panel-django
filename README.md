# New-admin-panel-django
New advanced admin panel in Django

Hello, this is a new flexible admin panel made in django

This way you don't create an admin panel for your project, you just enter the model.

Things to do:
    1) pip install -r requirements.txt
     2) Add dashboard and templates/dashboard to your project

Enter the data in the .env file:
     ADMIN='Username'
     PASSWORD='Password'
     COOKIE = is_admin

Add the dashboard url to the project management part ( config ).
Check the result.

If so, go to dashboard.admin.py
     ADMIN_REGISTER = [
          {'model': Model'},
                 {'model': Model2'},
     ]

log in and the admin panel is ready.


Thank you very much for your attention!
