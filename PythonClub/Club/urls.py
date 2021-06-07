from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('meetings/', views.meetings, name = 'meetings'),
   path('details/<int:id>', views.details, name='details'),
   path('newmeeting/', views.newMeeting, name='newmeeting'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),   

]