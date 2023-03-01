from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.

# Previous admin panel register
# >>> admin.site.register(User)



# New admin panel register
ADMIN_REGISTER = [
	{'model': User, 'name': 'user'},
]