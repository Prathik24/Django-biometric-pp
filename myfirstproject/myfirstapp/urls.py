from django.urls import path
from . import views


urlpatterns = [
    path('', views.myfunctioncall, name="index"),
    path('about', views.myfunctionabout, name="about"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('multiply/<int:c>/<int:d>', views.mult, name='mult'),
    path('mysecondpage' , views.mysecondpage,name='mysecondpage'),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('mythirdpage' , views.mythirdpage,name = 'mythirdpage'),
    path('Myimagepage',views.myimagepage,name='myimagepage'),
    path('myimagepage2',views.myimagepage2,name='imagepage2'),
    path ('myform' , views.myform,name='myform'),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('myform2',views.myform2,name='myform2'),









]
