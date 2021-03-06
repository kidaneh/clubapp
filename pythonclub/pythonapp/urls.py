from django.urls import path
from . import views
#
urlpatterns=[
  path('', views.index, name='index'),
  path('getResource/', views.getResource, name='resource'),
  path('getmeetings/', views.getmeetings, name='meetings'),
  path('meetdetails/<int:id>', views.meetingdetails, name='meetdetails'),
  path('newMeeting/', views.newMeeting, name='newmeeting'),
  path('loginmessage/', views.loginmessage, name='loginmessage'),
  path('logoutmessage/', views.logoutmessage, name='logoutmessage')

]