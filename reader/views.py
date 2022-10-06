from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from transactions.models import Transaction

from reader.serializers import ReaderSerializer

from .forms import CNBAForm, UploadFileForm


class HomeView(APIView):
    def post(self, request: Request) -> Response:
        # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
        # form = CNBAForm(request.POST, request.FILES)
        # import ipdb

        # ipdb.set_trace()

        # serializer.save()
        form = UploadFileForm(request.POST, request.FILES)
        # form = CNBAForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # with open(request.FILES["file"], "r") as file:
            # for line in request.FILES["file"]:
            for line in request.FILES["file"]:
                text = (
                    line.decode("unicode_escape")
                    .encode("latin1")
                    .decode("utf8")
                )
                tipo = Transaction.objects.get(tipo=text[0:1])

                print(tipo)
                data = {
                    "tipo": tipo,
                    "data": f"{text[1:5]}/{text[5:7]}/{text[7:9]}",
                    "valor": float(text[9:19]) / 100,
                    "cpf": text[19:30],
                    "cartao": text[30:42],
                    "hora": f"{text[42:44]}:{text[44:46]}:{text[46:48]}",
                    "dono_da_loja": text[48:62].strip(),
                    "nome_da_loja": text[62:81].strip(),
                }
                import ipdb

                ipdb.set_trace()
                # serializer = ReaderSerializer(data={
                #     tipo:tipo,
                #     data=text[2:8]
                # })
                # serializer.is_valid(raise_exception=True)

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
