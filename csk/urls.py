
from csk.views import *
from django.urls import path
app_name='chennai super kings' 
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('jadeja/',jadeja,name='jadeja'),
]