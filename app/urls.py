
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
   path('likeBtn_action/<int:food_id>/', views.likeBtn_action, name='likeBtn_action'),
   path('dislikeBtn_action/<int:food_id>/', views.dislikeBtn_action, name='dislikeBtn_action'),
    path('like/<int:card_id>/', views.like_food, name='like_food'),
    path('dislike/<int:card_id>/', views.dislike_food, name='dislike_food'),
]
