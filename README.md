# New-admin-panel-django
New advanced admin panel in Django


Hello, this is a new flexible admin panel made in django

This way you don't create an admin panel for your project, you just enter the model.
### Installation
> `pip install -r requirements.txt`

### Things to do
     * Add the dashboard and templates/dashboard folders to your project
     * and create a .env file

### Enter the data in the .env file:
    
     ADMIN='Username'
     PASSWORD='Password'
     COOKIE = is_admin  #default
    

Add the dashboard url to the project management part ( config ).
Check the result.

![alt text](![New-admin-panel-django-home-image](https://user-images.githubusercontent.com/120723170/222183187-6c47dae0-bc9d-4c9d-b735-359aabb03425.jpg))


#### If so, go to dashboard.admin.py
     ADMIN_REGISTER = [
          {'model': Model'},
          {'model': Model2'},
     ]

enter it like this and the admin panel is ready.



Thank you very much for your attention!
