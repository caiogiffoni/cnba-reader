from django import forms


class CNBAForm(forms.Form):
    file = forms.FileField()


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
