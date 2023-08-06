
from django.contrib import admin
from django.urls import path
from app.views import home , login , signup , signout 
from . import views

urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup, name='signup' ), 
   path('logout/' , signout, name='signout' ), 
   path('resume/', views.resume, name='resume'),
   path('uploadFoodCard/', views.add_todo, name='uploadFoodCard'),
   
]
