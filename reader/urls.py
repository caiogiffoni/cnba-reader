from django.urls import path

from reader.views import HomeView, TableView

urlpatterns = [
    path("home/", HomeView.as_view()),
    path("table/", TableView.as_view()),
]
