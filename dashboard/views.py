from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from data.config import read_env
from .forms import ModelFormFunc
from .functions import (
		ModelsData, obj_filt, IsAdmin,
		 ModelDeleteFunc, AdminLogin, AdminLogout,
		 SearchModel, UpdateAdmin)
from .admin import ADMIN_REGISTER

# Create your views here.

# ------------------------------- Home ---------------------------
class Home(IsAdmin, View):
	def get(self, request):
		data = {'ADMIN_REGISTER':ADMIN_REGISTER}
		return render(request, 'dashboard/home.html', data)


# ---------------------------- View model -------------------------------
class ModelView(IsAdmin, View):
	def get(self, request, model):
		data = {}
		model_all_data = ModelsData().all_(request, unique_name=str(model))
		data['page_obj'] = model_all_data

		search = request.GET.get("search")
		if search:
			table = ModelsData().get_(unique_name=str(model))['model']

			filter = SearchModel(request, table, search)
			data['page_obj'] = filter
			data['search'] = search

		
		data['model'] = model
		data['ADMIN_REGISTER'] = ADMIN_REGISTER
		return render(request, 'dashboard/model/view.html', data)

	def post(self, request, model):
		if request.POST.get("action").lower() == 'delete':
			table = ModelsData().get_(unique_name=str(model))['model']
			messages.info(request, f"{model} delete")

			if request.POST.get("checkbox_"):
				ids = dict(request.POST).get("checkbox_")
				ModelDeleteFunc(model, ids)

		
		return redirect("dashboard:modelview", model)


# ----------------------- Model add view --------------------------------
class ModelAddView(IsAdmin, View):
	def get(self, request, model):
		table = ModelsData().get_(unique_name=str(model))['model']
		form = ModelFormFunc(table)

		data = {'form':form, 'ADMIN_REGISTER': ADMIN_REGISTER,
			'model':model}
		return render(request, 'dashboard/model/add.html', data)

	def post(self, request, model):
		table = ModelsData().get_(unique_name=str(model))['model']
		form = ModelFormFunc(
					table, 
					data=request.POST,
					files=request.FILES)

		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			messages.info(request, f"{model} add")
			if request.POST.get("_save_and_add"):
				return redirect("dashboard:modeladd", model)

			if request.POST.get("_save_and_edit"):
				return redirect("dashboard:change", model, data.id)

			return redirect("dashboard:modelview", model)
		else:
			data = {'form':form, 'ADMIN_REGISTER':ADMIN_REGISTER,
					'model':model}
			return render(request, "dashboard/model/add.html", data)


# ---------------------------------- Change view ----------------------
class ChangeView(IsAdmin, View):
	def get(self, request, model, id):
		table = ModelsData().get_(unique_name=str(model))['model']
		form = ModelFormFunc(model=table, instance=obj_filt(model, id))
		
		data = {
			'form':form, 'ADMIN_REGISTER': ADMIN_REGISTER,
			'model':model}
		return render(request, "dashboard/model/change.html", data)

	def post(self, request, model, id):
		table = ModelsData().get_(unique_name=str(model))['model']
		if request.POST.get("_delete"):
			ModelDeleteFunc(model, id)
			messages.info(request, f"{model} delete")
			return redirect("dashboard:modelview", model)

		model_ = table
		form = ModelFormFunc(
			model=model_,
			instance=obj_filt(model, id),
			data=request.POST,
			files=request.FILES)
		if form.is_valid():
			form.save()

			if request.POST.get("_save_and_add"):
				return redirect("dashboard:modeladd", model)

			if request.POST.get("_save_and_edit"):
				return redirect("dashboard:change", model, id)

			messages.info(request, f"{model} change")
			return redirect("dashboard:modelview", model)
		else:
			data = {'form':form, 'ADMIN_REGISTER':ADMIN_REGISTER,
				'model':model}
			return render(request, "dashboard/model/change.html", data)

# -------------------------- Profile Update ---------------------
class ProfileUpdateView(IsAdmin, View):
	def get(self, request):

		data = {
			'username':read_env()['ADMIN'],
			'password':read_env()['PASSWORD'],
			'ADMIN_REGISTER':ADMIN_REGISTER}
		return render(request, "dashboard/user/update.html", data)

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')

		update = UpdateAdmin(username, password, "dashboard:profileupdate")
		messages.info(request, "Admin change")
		if update:
			return update

		return redirect("dashboard:profileupdate")


# --------------------- Login ---------------------------
class LoginView(View):
	def dispatch(self, request):
		if request.method == "GET":
			return self.get(request)
		if request.method == "POST":
			return self.post(request)

	def get(self, request):
		return render(request, 'dashboard/user/login.html', {})

	def post(self, request):
		username = request.POST.get("username")
		password = request.POST.get("password")

		login = AdminLogin(username=username, password=password, redirect_url="dashboard:home")
		if login:
			messages.info(request, "Welcom.")
			return login

		error_message = "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."
		messages.error(request, error_message)
		return redirect("dashboard:login")


# -------------------------------- Logout ----------------------
class LogoutView(IsAdmin, View):
	def get(self, request):
		logout = AdminLogout(redirect_url="dashboard:login")

		messages.info(request, "Logout")
		return logout