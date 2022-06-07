from django.db import models
from django.db.models import JSONField


class DataToSave(models.Model):
    """This model only used to save data to DB"""
    data = JSONField()
