import json
import re

from django.shortcuts import render, redirect

# from .connection import save_to_db
from .forms import DataFormSet
from .models import DataToSave


def create_form(request):
    """The main func to work with form

    This function is used to process a request
    and save data to DB.
    One thing I should notice: every data from form
    is saving by personal connection. Maybe this is probably
    not true for large applications, but it is made to print
    into console the data from every form without using a loop
    """
    # creating the instance of Formset
    formset = DataFormSet(request.POST or None)
    context = {
        'formset': formset,
    }
    # iteration over a formset
    for form in formset:
        # this "if" is used to work with only post method
        if request.method == 'POST':
            # if this particular form is valid,
            # we can work with it
            if form.is_valid():
                # this loop looking for the pattern from
                # the queryset
                for key, value in request.POST.items():
                    if re.search('form-'+r'\d*'+'-data', key):
                        # if we find the match, we convert
                        # result to json and save to data
                        DataToSave.objects.create(data=json.dumps(value))
                        print(f'Data with values {value} is added')
                        # the code below save_to_db()
                        # is used to connect to db
                        # without django orm
                        # save_to_db(data_json)
            return redirect('create-form')
    return render(request, 'forms/create_data.html', context)


def show_data(request):
    """Func to render data from db"""
    # In this case there wasn't requirements how to display data
    # I decided to reconvert values to the string to show it

    # iterate over the queryset data to get values to reconvert it
    data_from_db = DataToSave.objects.all().values()
    for row in data_from_db:
        if row['data'] == '""':
            # If there was no entered information, we display the text
            row['data'] = 'Nothing entered'
        # deleting quotes
        row['data'] = row['data'].strip('"')
    context = {
        'data_from_db': data_from_db
    }
    return render(request, 'forms/show_data.html', context)