from django.urls import path

from . import views
from .templatetags import filters

app_name = 'main_webform'
urlpatterns = [
    path('', views.model_form_upload, name='model_form_upload'),
    path('text', views.model_form_upload, name='text'),
   # path('text', filters.highlight, name='text'),
]
