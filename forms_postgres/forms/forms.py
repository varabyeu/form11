from django import forms
from django.forms import formset_factory


class DataForm(forms.Form):
    data = forms.CharField(max_length=255)


DataFormSet = formset_factory(DataForm)
