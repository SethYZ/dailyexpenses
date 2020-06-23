from django.urls import path
from . import views
from .views import ExpensesListView, ExpensesDetailView

urlpatterns = [
path("", views.home_view, name="main-home"),
path("index/", views.index_view, name="main-index"),
path("create/", views.create, name="main-create"),
path("view/", views.list, name="list"),
path("list/", ExpensesListView.as_view(), name="listview"),
path("listdetail/", ExpensesDetailView.as_view(), name="listdetail"),
]
