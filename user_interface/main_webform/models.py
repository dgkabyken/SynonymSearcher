import datetime

from django.db import models
from django.utils import timezone
from django import forms

class Document(models.Model):
    word_to_search = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    document = models.FileField(upload_to='media', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
