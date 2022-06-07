from django.urls import path

from forms.views import create_form, show_data

urlpatterns = [
    path('', create_form, name='create-form'),
    path('show/', show_data, name='show-data')
]
