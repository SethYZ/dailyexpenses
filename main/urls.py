from django.urls import path
from . import views

urlpatterns = [
path("", views.home_view, name="main-home"),
path("index/", views.index_view, name="main-index"),
path("create/", views.create, name="main-create"),
path("view/", views.list, name="list")
]
