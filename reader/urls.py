from django.urls import path

from reader.views import HomeView

urlpatterns = [
    path("home/", HomeView.as_view()),
]
