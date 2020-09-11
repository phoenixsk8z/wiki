from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.search, name="search"),
    path("query", views.query, name="query"),
    path("createpage", views.createpage, name="createpage"),
]
