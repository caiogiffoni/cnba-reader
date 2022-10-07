from functools import total_ordering

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from transactions.models import Transaction

from reader.models import Reader
from reader.serializers import ReaderSerializer, ReaderSerializerView

from .forms import UploadFileForm


class HomeView(APIView):
    # if this is a POST request we need to process the form data
    def post(self, request: Request) -> Response:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for line in request.FILES["file"]:  # ADJUST STRING FOR ACCENTS
                text = (
                    line.decode("unicode_escape")
                    .encode("latin1")
                    .decode("utf8")
                )
                tipo = Transaction.objects.get(tipo=text[0:1])
                # PARSING INFO TO DATA
                data = {
                    "data": f"{text[1:5]}-{text[5:7]}-{text[7:9]}",
                    "valor": float(text[9:19]) / 100,
                    "cpf": text[19:30],
                    "cartão": text[30:42],
                    "hora": f"{text[42:44]}:{text[44:46]}:{text[46:48]}",
                    "dono_da_loja": text[48:62].strip(),
                    "nome_da_loja": text[62:81].strip(),
                    "tipo": tipo.id,
                }
                serializer = ReaderSerializer(data=data)
                serializer.is_valid(raise_exception=True),
                serializer.save()
            return HttpResponseRedirect("/table/")
        return render(request, "home.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    def get(self, request: Request) -> Response:
        form = UploadFileForm()
        return render(request, "home.html", {"form": form})


class TableView(APIView):
    def get(self, request: Request) -> Response:
        serializer = ReaderSerializerView(Reader.objects.all(), many=True)
        stores = {x["nome_da_loja"] for x in serializer.data}
        total_transaction = {}
        for store in stores:  # TRANSACTION TOTAL FOR EACH STORE
            total_transaction[store] = sum(
                [
                    float(transaction["valor"])
                    for transaction in serializer.data
                    if transaction["nome_da_loja"] == store
                ]
            )
        return render(
            request,
            "table.html",
            {
                "response": serializer.data,
                "stores": total_transaction,
            },
        )
