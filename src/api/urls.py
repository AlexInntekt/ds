from django.contrib import admin
from django.urls import path, include
from .views import UsersView


urlpatterns = [
	path('/users', UsersView.as_view(), name="list_users"),
]