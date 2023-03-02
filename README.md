# New-admin-panel-django
New advanced admin panel in Django <br />


Hello, this is a new flexible admin panel made in django
This way you don't create an admin panel for your project, you just enter the model.<br />


### Installation
> `pip install -r requirements.txt`

### Things to do
     * Add the dashboard and templates/dashboard folders to your project
     * and create a .env file

### Enter the data in the .env file:
    
     ADMIN='Username'
     PASSWORD='Password'
     COOKIE = is_admin  #default
    
Add the control panel URL to the project control section ( config.urls ).
    `
    urlpatterns = [
        path('admin/', admin.site.urls),
        # new admin panel
        path('dashboard/', include('dashboard.urls')),
    ]
    `

Check the result. (http://127.0.0.1:8000/dashboard/) <br />
And you will have a login window. Then enter these details
 * username = env.ADMIN
 * passwrod = env.PASSWORD

![New-admin-panel-django-home-image](https://user-images.githubusercontent.com/120723170/222183187-6c47dae0-bc9d-4c9d-b735-359aabb03425.jpg)

#### If so, go to the dashboard.admin.py file
     ADMIN_REGISTER = [
          {'model': Model'},
          {'model': Model2'},
     ]

enter it like this and the admin panel is ready. <br /><br />



Thank you very much for your attention!
