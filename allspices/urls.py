from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("register",views.register, name="register"),
    path("create/new",views.create, name="create"),
    path("favourite",views.favourite, name="favourite"),
    path("comment/new",views.comment, name="comment"),
    path("favor/<int:id>/add",views.add_favourite,name="add_favourite"),
    path("favor/<int:id>/del",views.del_favourite, name="del_favourite"),
    path("details/<int:id>",views.details, name="details"),
    path("category",views.category, name="category")
]