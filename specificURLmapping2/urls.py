from specificURLmapping2.views import *
from django.urls import path

app_name='second'
urlpatterns=[
        path('specific2/',specific2,name='specific2')
]
