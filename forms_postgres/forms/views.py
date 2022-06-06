import json

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .connection import save_to_db

from .forms import DataFormSet


class BirdListView(ListView):
    template_name = 'bird_list.html'


def create_form(request):
    formset = DataFormSet(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            data_from_form = {
                str(id(formset)): formset.cleaned_data[0]['data'],
            }
            data_json = json.dumps(data_from_form)
            save_to_db(data_json)
        return redirect('create-form')
    context = {
        'formset': formset,
    }
    return render(request, 'forms/create_data.html', context)
