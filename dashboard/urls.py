from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/', views.dashboard, name='myprofile'),
    path('editprofile/', views.editprofile, name='edit_profile'),
    path('changePassword/', views.changePassword, name='changePassword'),

    path('myproducts/', views.myproducts, name='myproducts'),
    path('managemypd/', views.managemypd, name='managemypd'),

]