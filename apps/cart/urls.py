from django.urls import include, path
from . import views

urlpatterns = [
    path('order/<int:id>', views.payOrder,name="payOrder"),
   	path('return/', views.returnWepayWebsite,name="returnWepayWebsite"),
   	path('final/', views.wepayFinalWebsite,name="wepayFinalWebsite"),
]
