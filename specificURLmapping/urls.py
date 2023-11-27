from specificURLmapping.views import *
from django.urls import path

app_name='something'
urlpatterns=[
    path('specific/',specific,name='specific') 
]