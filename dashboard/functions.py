from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.db.models import CharField
from django.db.models import  Q
from django.core.paginator import Paginator
from django.contrib import messages

import dotenv
import os 
from datetime import datetime, timedelta

from .admin import ADMIN_REGISTER
from data.config import  COOKIE, read_env


LOGIN_URL = "dashboard:login"


# Page
def Page(request, model, page_size=31):
	# Paginator
	page_size = request.GET.get('page_size', page_size)
	paginator = Paginator(model, page_size)
	page_num = request.GET.get('page', 1)
	page = paginator.get_page(page_num)

	return page


# Admin register
class ModelsData:
	def get_(self, unique_name):
		for dict_data in ADMIN_REGISTER:
			# Model name read
			name = dict_data['model']._meta.verbose_name

			if str(name) == str(unique_name):
				return dict_data

	def all_(self, request, unique_name):

		for dict_data in ADMIN_REGISTER:
			# Model name read
			name = dict_data['model']._meta.verbose_name

			if str(name) == str(unique_name):
				model = dict_data['model'].objects.all().order_by('-id')
				# Paginator
				page_obj = Page(request, model)

				return page_obj


# Is admin
class IsAdmin(AccessMixin):
	def dispatch(self, request, *args, **kwargs):
		cookie = request.COOKIES.get(COOKIE)
		if not cookie == read_env()['PASSWORD']:
			return redirect(LOGIN_URL)

		try:
			return super().dispatch(request, *args, **kwargs)
		except Exception as e:
			print(e)
			messages.error(request, "Error")
			return redirect("dashboard:home")

# obj
def obj_filt(model, al):
	table = ModelsData().get_(unique_name=str(model))

	model_ = table['model'].objects.get(id=al)
	return model_


# Model delete function
def ModelDeleteFunc(model, ids):
	model_ = ModelsData().get_(unique_name=str(model))
	try:
		if type(ids) == int or type(ids) == str:
			delete = model_['model'].objects.get(id=int(ids))
			delete.delete()

			return True

		# ids > 1 
		for id in ids:
			delete = model_['model'].objects.get(id=int(id))
			delete.delete()

		return True
	except Exception as e:
		return False

# Search table
def SearchModel(request, table, search):
	fields = [f for f in table._meta.fields if isinstance(f, CharField)]
	queries = [Q(**{f.name+'__contains': search}) for f in fields]
	qs = Q()

	for query in queries:
		qs = qs | query

	data = table.objects.filter(qs)
	response = Page(request, data)
	return response



# Login function
def AdminLogin(username, password, redirect_url):
	ADMIN = read_env()['ADMIN']
	PASSWORD = read_env()['PASSWORD']
	if str(username) == str(ADMIN) and str(password) == str(PASSWORD):
		response = redirect(redirect_url)
		response.set_cookie(
			COOKIE,
			PASSWORD,
			expires=datetime.utcnow() + timedelta(days=360))
		return response
	else:
		return False


# Logout function
def AdminLogout(redirect_url):
	response = redirect(redirect_url)
	response.delete_cookie(COOKIE)
	return response


# Update ADMIN and PASSWORD
def UpdateAdmin(username, password, redirect_url):
	dotenv_file = dotenv.find_dotenv()
	dotenv.load_dotenv(dotenv_file)

	os.environ["ADMIN"] = username 
	os.environ["PASSWORD"] = password 

	# Write changes to .env file.
	dotenv.set_key(dotenv_file, "ADMIN", os.environ["ADMIN"])
	dotenv.set_key(dotenv_file, "PASSWORD", os.environ["PASSWORD"])

	# login
	login = AdminLogin(username=os.environ["ADMIN"], password=os.environ["PASSWORD"],
						redirect_url=redirect_url)
	return login
