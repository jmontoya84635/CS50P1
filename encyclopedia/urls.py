from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.searchResult, name="searchResult"),
    path("search", views.searchBar, name="searchBar")
]
