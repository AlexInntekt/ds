from django.contrib import admin
from django.urls import path, include
from .views import UsersView, SensorView


urlpatterns = [
    path('/users', UsersView.as_view(), name="list_users"),
    path('/sensor/<int:sensor>', SensorView.as_view(), name="sensor"),
]