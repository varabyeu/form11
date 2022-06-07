from django import forms
from django.forms import formset_factory


class DataForm(forms.Form):
    # The created form was made with one input
    data = forms.CharField(max_length=255)


# formset_factory is used to make a set of forms
DataFormSet = formset_factory(DataForm)
