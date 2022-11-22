from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/', views.dashboard, name='myprofile'),
    path('editprofile/', views.editprofile, name='edit_profile'),
    path('changePassword/', views.changePassword, name='changePassword'),

    path('myproducts/', views.myproducts, name='myproducts'),
    path('managehouse/<int:house_id>/', views.managehouse, name='managehouse'),
    path('managecar/<int:car_id>/', views.managecar, name='managecar'),
    path('managebike/<int:bike_id>/', views.managebike, name='managebike'),
    path('managefurniture/<int:furniture_id>/', views.managefurniture, name='managefurniture'),
    path('manageother/<int:other_id>/', views.manageother, name='manageother'),

]