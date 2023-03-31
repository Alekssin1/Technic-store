from django.urls import path
from . import views

urlpatterns = [
 path('', views.Home.as_view(), name='home'),
 path('register/', views.Register.as_view(), name='register'),
 path('login/phone/', views.LoginPhone.as_view(), name='login_phone'),
 path('login/email/', views.LoginEmail.as_view(), name='login_email'),
 path('logout/', views.logout_acc, name='logout'),
 path('addbin/<int:id>/', views.addbin, name='addBin'),
 path('dellbin/<int:id>/', views.del_bin_item, name='dellBin'),
]

