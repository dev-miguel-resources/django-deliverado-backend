from django.contrib import admin
from django.urls import path,include

from . import views
 
urlpatterns = [
    
    #NEW HTML

    path('', views.homeMaster ,name="homeMaster"), 
   

]

