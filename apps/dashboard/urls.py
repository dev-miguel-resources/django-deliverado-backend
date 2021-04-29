from django.contrib import admin
from django.urls import path,include

from . import views
 
urlpatterns = [
    
     
	
    #User
   
    path('logout/', views.logoutDashboard ,name="logoutDashboard"),

     


    #NEW HTML

    path('', views.home ,name="home"), 
    path('order/pending/<pk>', views.viewOrderPendingDashboard ,name="viewOrderPendingDashboard"),
    path('order/pending/update/delivery/<pk>/<userid>/', views.updateDeliveryOrderDashboard ,name="updateDeliveryOrderDashboard"),
    path('order/pending/update/cookingtime/<pk>/<minutes>/', views.updateCookingTimeOrderDashboard ,name="updateCookingTimeOrderDashboard"),
    path('order/cancel/<pk>', views.cancelOrderDashboard ,name="cancelOrderDashboard"),
    path('order/accept/<pk>', views.acceptOrderDashboard ,name="acceptOrderDashboard"),
    path('order/proccessing/<pk>', views.viewOrderProcessingDashboard ,name="viewOrderProcessingDashboard"),
    path('order/startcooking/<pk>', views.startCookingOrderDashboard ,name="startCookingOrderDashboard"),
    path('order/cancel/delivery/<pk>', views.cancelDeliveryOrderDashboard ,name="cancelDeliveryOrderDashboard"),



    
   
    path('menu/', views.menu ,name="menu"), 
    path('menu/experiencias/', views.menuExperiencias ,name="menuExperiencias"), 
    path('menu/add/product/', views.createProductDashboard ,name="createProductDashboard"),
    path('menu/view/product/<pk>/', views.viewProductDashboard ,name="viewProductDashboard"),
    path('menu/update/product/<pk>/', views.updateProductDashboard ,name="updateProductDashboard"),
    path('users/', views.listUsersDashboard ,name="listUsersDashboard"),
    path('users/add/operator', views.createOperatorUsersDashboard ,name="createOperatorUsersDashboard"), 
    path('users/update/operator/<pk>', views.updateOperatorUsersDashboard ,name="updateOperatorUsersDashboard"), 
    path('users/add/delivery', views.addDeliveryUserDashboard ,name="addDeliveryUserDashboard"), 

    path('profile/', views.profileDashboard ,name="profileDashboard"), 
    path('profile/open/shop/', views.openShop ,name="openShop"), 
    path('profile/close/shop/', views.closeShop ,name="closeShop"), 

    

    #no funcionales
    path('balance/', views.balance ,name="balance"), 
    
    path('pedidos-aceptados/', views.pedidosAceptados ,name="pedidosAceptados"), 
    path('pedidos-entregados/', views.pedidosEntregados ,name="pedidosEntregados"), 
    path('pedidos-cancelados/', views.pedidosCancelados ,name="pedidosCancelados"), 
    path('exp-pedidos-pendientes/', views.expPedidosPendientes ,name="exppedidosCancelados"), 
    path('exp-pedidos-aceptados/', views.expPedidosAceptados ,name="expPedidosAceptados"),
    path('repartidor-pedidos-pendientes/', views.repartidorPedidosPendientes ,name="repartidorPedidosPendientes"), 
    path('editar-plato/', views.editarPlato ,name="editarPlato"),
    path('editar-exp/', views.editarExp ,name="editarExp"), 
    path('agregar-nueva-exp/', views.agregarNuevaExp ,name="agregarNuevaExp"), 
    path('promociones/', views.promociones ,name="promociones"), 
    path('tipo-de-promocion/', views.tipoDePromocion ,name="tipoDePromocion"), 
    path('promocion-por-porcentaje/', views.promocionPorPorcentaje ,name="promocionPorPorcentaje"),
    path('promocion-2-1/', views.promocion2x1 ,name="promocion2x1"), 
    path('promocion-envio-gratis/', views.promocionEnvioGratis ,name="promocionEnvioGratis"), 
    path('promocion-agregar-platos/', views.promocionAgregarPlatos ,name="promocionAgregarPlatos"), 
    path('promocion-agregar-acompanantes/', views.promocionAgregarAcom ,name="promocionAgregarAcom"), 
    path('editar-promocion/', views.editarPromocion ,name="editarPromocion"), 
    path('editar-promocion-plato/', views.editarPromocionAgregarPlato ,name="editarPromocionAgregarPlato"),
    path('editar-promocion-acom/', views.editarPromocionAgregarAcom ,name="editarPromocionAgregarAcom"), 
    
 
    path('nuevo-login/', views.nuevoLogin ,name="nuevoLogin"), 
    path('nuevo-registro/', views.nuevoRegistro ,name="nuevoRegistro"), 
    path('recuperar-contrasena/', views.recuperarContraseña ,name="recuperarContraseña"), 
    path('restaurar-contrasena/', views.restaurarContraseña ,name="restaurarContraseña"), 

]

