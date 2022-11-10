from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.Category, name='category'),
    path('add_house/', views.add_house, name='add_house'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_bike/', views.add_bike, name='add_bike'),
    path('add_furn/', views.add_furn, name='add_furn'),
    path('add_other/', views.add_other, name='add_other'),

]