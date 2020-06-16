from django.urls import path
from . import views

urlpatterns = [
path("", views.home_view, name="main-home"),
path("<int:id>", views.index, name="index"),
path("create/", views.create, name="create"),
path("view/", views.list, name="list")
]
