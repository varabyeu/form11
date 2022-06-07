import json
import re

from django.shortcuts import render, redirect

from .connection import save_to_db
from .forms import DataFormSet


def create_form(request):

    formset = DataFormSet(request.POST or None)
    context = {
        'formset': formset,
    }
    for form in formset:
        if request.method == 'POST':
            if form.is_valid():
                for key, value in request.POST.items():
                    if re.search('form-'+r'\d*'+'-data', key):
                        data_json = json.dumps(value)
                        save_to_db(data_json)
            return redirect('create-form')
    return render(request, 'forms/create_data.html', context)
