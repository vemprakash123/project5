from mi.views import *
from django.urls import path
app_name='mumbai indians'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumrah/',bumrah,name='bumrah'),
]