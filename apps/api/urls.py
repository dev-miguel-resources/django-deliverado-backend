from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url


from rest_framework.authtoken.views import obtain_auth_token



from rest_framework import permissions
 

from . import views


 

urlpatterns = [
    
    #custom
    path('auth/', obtain_auth_token), #login old
    

    
    path('login/mobile/', views.LoginMobile.as_view()), #login new
    path('my/token/', views.MyToken.as_view()), #get token

    path('hasvehicle/', views.HasVehicleView.as_view()), #get token



    path('register/', views.UserCreate.as_view()),
    path('profile/', views.CurrentUserView.as_view()),

    path('reset_password/', views.reset_password.as_view()), #DRP  - TOKEN



    path('requestchangepassword/', views.RequestChangePassword.as_view()), # WITH SMS OR CODE
    path('changepassword/', views.ChangePassword.as_view()), # WITH SMS OR CODE
    
    #models
    path('users/', views.UserList.as_view()),  
    path('users/<pk>', views.UserDetail.as_view()),
    path('users/noavatar/<pk>', views.UserDetailNoAvatar.as_view()),
    path('validatecode/', views.ValidateCode.as_view()),

    path('validateqr/', views.ValidateQR.as_view()),
    
    

    path('address/', views.AddressUserList.as_view()),  
    path('address/<pk>', views.AddressUserDetail.as_view()),

    path('experience/', views.ExperienceList.as_view()),  
    path('experience/<pk>', views.ExperienceDetail.as_view()),
   
    path('experience/product/', views.ExperienceProductList.as_view()),  
    path('experience/product/<pk>', views.ExperienceProductDetail.as_view()),

    path('category/', views.CategoryList.as_view()),  
    path('category/<pk>', views.CategoryDetail.as_view()),

    path('category/product/', views.CategoryProductList.as_view()),  
    path('category/product/<pk>', views.CategoryProductDetail.as_view()),

    
   
    path('shop/search', views.ShopSearch.as_view()),  
    path('shop/', views.ShopList.as_view()),  
    path('shop/<pk>', views.ShopDetail.as_view()),


    path('shop/list/category/', views.ListCategoryShop.as_view()),  
    

    
    path('category/group/', views.CategoryGroupList.as_view()),  
    path('category/group/<pk>', views.CategoryGroupDetail.as_view()),

 

    path('product/', views.ProductList.as_view()),  
    path('product/<pk>', views.ProductDetail.as_view()),


    path('product/featured/', views.FeaturedProductList.as_view()),  
    path('product/featured/<pk>', views.FeaturedProductDetail.as_view()),

    path('shop/promotion/', views.PromotionShopList.as_view()),  
    path('shop/promotion/<pk>', views.PromotionShopDetail.as_view()),

    path('shop/featured/', views.FeaturedShopList.as_view()),  
    path('shop/featured/<pk>', views.FeaturedShopDetail.as_view()),

    path('order/', views.OrderList.as_view()),  
    path('order/<pk>', views.OrderDetail.as_view()),
    path('order/adddriver/<pk>', views.OrderAddDriverDetail.as_view()),
    path('order/address/<pk>', views.OrderAddressDetail.as_view()),
    path('order/getlastorder/', views.GetLastOrder.as_view()),  
    path('order/getcartorder/', views.GetCartOrder.as_view()),  
    
    path('order/history/status/', views.OrderHistoryStatusList.as_view()), 

    path('order/filter/dates/', views.OrderFilterDates.as_view()),  

    path('order/product/', views.OrderProductList.as_view()),  
    path('order/product/add/', views.AddOrderProductList.as_view()),  
    path('order/product/<pk>', views.OrderProductDetail.as_view()),

    path('order/message/', views.MessageOrderList.as_view()),  
    path('order/message/add/', views.AddMessageOrderList.as_view()),  
    path('order/message/<pk>', views.MessageOrderDetail.as_view()),

    path('order/feedback/', views.FeedbackOrderList.as_view()),  
    path('order/feedback/<pk>/', views.FeedbackOrderDetail.as_view()),  

    path('order/report/', views.ReportOrderList.as_view()),  
    path('order/report/<pk>', views.ReportOrderDetail.as_view()),

    path('vehicle/', views.VehicleList.as_view()),  
    path('vehicle/<pk>', views.VehicleDetail.as_view()),

    path('gps/', views.DataGPSList.as_view()),  
    path('gps/<pk>/', views.DataGPSDetail.as_view()), 

    path('distancetime/', views.GetDistanceTime.as_view()),  
    

]
