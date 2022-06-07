from django.urls import path

from forms.views import create_form

urlpatterns = [
    path('', create_form, name='create-form'),
]
