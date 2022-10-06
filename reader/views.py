from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from reader.serializers import ReaderSerializer

from .forms import CNBAForm, UploadFileForm


class HomeView(APIView):
    def post(self, request: Request) -> Response:
        # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
        # form = CNBAForm(request.POST, request.FILES)
        # import ipdb

        # ipdb.set_trace()

        serializer.save()
        form = UploadFileForm(request.POST, request.FILES)
        # form = CNBAForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # with open(request.FILES["file"], "r") as file:
            # for line in request.FILES["file"]:
            for line in request.FILES["file"]:
                # import ipdb

                # ipdb.set_trace()
                text = (
                    line.decode("unicode_escape")
                    .encode("latin1")
                    .decode("utf8")
                )
                tipo = text[0:1]
                Transaction
                serializer = ReaderSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                print(text)

            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")
        return render(request, "home.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    def get(self, request: Request) -> Response:
        # form = CNBAForm()
        form = UploadFileForm()

        return render(request, "home.html", {"form": form})
