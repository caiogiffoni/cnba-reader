from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

# Create your views here.


class HomeView(APIView):
    def get(self, request: Request) -> Response:
        return render(request, "home.html")
