from django.urls import path

from .views import (
	Home,
	LoginView,
	ModelView,
	ModelAddView,
	ChangeView,
	LogoutView,
	ProfileUpdateView,
)


app_name = "dashboard"
urlpatterns = [
		
	path('', Home.as_view(), name="home"),

	path('login/',
			LoginView.as_view(),name="login"),
	path('logout/',
			LogoutView.as_view(),name="logout"),
	path('profile/update',
			ProfileUpdateView.as_view(),name="profileupdate"),

	path('<str:model>/add/',
			ModelAddView.as_view(), name="modeladd"),
	path('<str:model>/view/', 
			ModelView.as_view(), name="modelview"),
	path('<str:model>/change/<int:id>/', 
			ChangeView.as_view(), name="change"),
]
