from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from apps.directory.models import *
from .forms import *
from django.template.defaulttags import register
from django.db.models import Avg, Count, Min, Sum

@register.filter()
def get_item(dictionary, key):
	return dictionary.get(key)






def logoutDashboard(request):
	logout(request)
	return redirect('/dashboard')


 

@login_required(login_url='nuevoLogin')
def home(request):
	

	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop
	
	list_order_new = Order.objects.filter(shop=shop,status = 1)
	list_order_proccessing = Order.objects.filter(shop=shop,status = 2) | Order.objects.filter(shop=shop,status = 4) | Order.objects.filter(shop=shop,status = 6)
	list_order_in_delivery =  Order.objects.filter(shop=shop,status = 7)
	list_order_cancel = Order.objects.filter(shop=shop,status = 5).count()
	list_order_complete = Order.objects.filter(shop=shop,status = 9).count()
 
	data = {
		
		"list_order_new":list_order_new,
		"list_order_proccessing":list_order_proccessing,
		"list_order_in_delivery":list_order_in_delivery,
		"shop":shop,
		"list_order_cancel":list_order_cancel,
		"list_order_complete":list_order_complete,
	}
	return render(request,'home.html',data)

@login_required(login_url='nuevoLogin')
def viewOrderPendingDashboard(request,pk):
	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop

	order = Order.objects.get(pk=pk)
	order_product = OrderProduct.objects.filter(order=pk).aggregate(total_product=Sum('quantity'))

	order_product_data = OrderProduct.objects.filter(order=pk)

 
	filter_users = [x.user.id for x in UserShop.objects.filter(shop=shop,user__type_user=1)]
	delivery_available = User.objects.filter(pk__in=filter_users)

	
	
	html = None

	
	data = {
		
		"order":order,
		"order_product":order_product,
		"order_product_data":order_product_data,
		"delivery_available":delivery_available,
	}
	return render(request,'viewOrderPendingDashboard.html',data)

@login_required(login_url='nuevoLogin')
def viewOrderProcessingDashboard(request,pk):
	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop

	order = Order.objects.get(pk=pk)
	order_product = OrderProduct.objects.filter(order=pk).aggregate(total_product=Sum('quantity'))

	order_product_data = OrderProduct.objects.filter(order=pk)

 
	filter_users = [x.user.id for x in UserShop.objects.filter(shop=shop,user__type_user=1)]
	delivery_available = User.objects.filter(pk__in=filter_users)

	
	
	html = None

	
	data = {
		
		"order":order,
		"order_product":order_product,
		"order_product_data":order_product_data,
		"delivery_available":delivery_available,
	}
	return render(request,'viewOrderProcessingDashboard.html',data)


@login_required(login_url='nuevoLogin')
def cancelOrderDashboard(request,pk):
	Order.objects.filter(pk=pk).update(status="3")
	return redirect('home')

@login_required(login_url='nuevoLogin')
def acceptOrderDashboard(request,pk):
	if Order.objects.filter(pk=pk)[0].user_delivery is None:
		Order.objects.filter(pk=pk).update(status="2")
	else:	
		Order.objects.filter(pk=pk).update(status="4")

	return redirect('home')

@login_required(login_url='nuevoLogin')
def updateDeliveryOrderDashboard(request,pk,userid):
	if userid == '0':
		Order.objects.filter(pk=pk).update(user_delivery=None)
	else:
		Order.objects.filter(pk=pk).update(user_delivery=User.objects.get(pk=userid))
	return redirect('viewOrderPendingDashboard',pk)

@login_required(login_url='nuevoLogin')
def updateCookingTimeOrderDashboard(request,pk,minutes):
	Order.objects.filter(pk=pk).update(cooking_time=minutes)
	return redirect('viewOrderPendingDashboard',pk)


@login_required(login_url='nuevoLogin')
def startCookingOrderDashboard(request,pk):
	Order.objects.filter(pk=pk).update(status="6")
	return redirect('home')

@login_required(login_url='nuevoLogin')
def cancelDeliveryOrderDashboard(request,pk):
	Order.objects.filter(pk=pk).update(status="5")
	return redirect('home')

@login_required(login_url='nuevoLogin')
def pedidosAceptados(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'pedidosAceptados.html',data)

@login_required(login_url='nuevoLogin')
def pedidosEntregados(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'pedidosEntregados.html',data)


@login_required(login_url='nuevoLogin')
def pedidosCancelados(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'pedidosCancelados.html',data)

@login_required(login_url='nuevoLogin')
def expPedidosPendientes(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'expPedidosPendientes.html',data)

@login_required(login_url='nuevoLogin')
def expPedidosAceptados(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'expPedidosAceptados.html',data)

@login_required(login_url='nuevoLogin')
def repartidorPedidosPendientes(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'repartidorPedidosPendientes.html',data)


@login_required(login_url='nuevoLogin')
def balance(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'balance.html',data)


@login_required(login_url='nuevoLogin')
def profileDashboard(request):
	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop

	if request.POST:
		form = updateProfileShopForm(request.POST,request.FILES,instance=shop)
		if form.is_valid() is True:
			form.save()
			return redirect('profileDashboard')
		else:
			import pdb; pdb.set_trace()
	
	else:
		form = updateProfileShopForm(instance=shop)
		data = {
			"shop":shop,
			"form":form,
		}
		return render(request,'profileDashboard.html',data)    


@login_required(login_url='nuevoLogin')
def	openShop(request):
	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop
	
	Shop.objects.filter(pk=shop.pk).update(status=1)

	return redirect('profileDashboard')

@login_required(login_url='nuevoLogin')
def closeShop(request):
	try:
		shop = Shop.objects.get(owner=request.user)
	except:
		shop = UserShop.objects.get(user=request.user).shop
	
	Shop.objects.filter(pk=shop.pk).update(status=0)

	return redirect('profileDashboard')		
		

@login_required(login_url='nuevoLogin')
def menu(request):
	shop = Shop.objects.get(owner=request.user)
	category_list = [ x.category_group for x in Product.objects.filter(shop = shop)]    
	category_list = list(dict.fromkeys(category_list))
	product_list = Product.objects.filter(shop = shop)
	
	html = None

	data = {
		"category_list":category_list,
		"product_list":product_list,
		"html":html,
	}
	return render(request,'menu.html',data)   

@login_required(login_url='nuevoLogin')
def menuExperiencias(request):
	shop = Shop.objects.get(owner=request.user)
	category_list = [ x.category_group for x in Product.objects.filter(shop = shop)]    
	category_list = list(dict.fromkeys(category_list))
	product_list = Product.objects.filter(shop = shop)
	
	html = None

	data = {
		"category_list":category_list,
		"product_list":product_list,
		"html":html,
	}
	return render(request,'menuExperiencias.html',data)   


@login_required(login_url='nuevoLogin')
def createProductDashboard(request):
	shop = Shop.objects.get(owner=request.user)
	if request.POST:
		
		form = createProductForm(request.POST,request.FILES)
		
		if form.is_valid() is True:
			f = form.save(commit=False)
			f.shop = shop
			f.category_group = CategoryGroup.objects.get(pk=(int(request.POST['category_group'])))
			f.save()
			return redirect('menu')
		else:
			pass
	else:
		category_list = [ x.category_group for x in Product.objects.filter(shop = shop)]    
		html = None
		form = createProductForm()
		data = {
			"form":form,
			"category_list":category_list,
			"html":html,
		}
		return render(request,'createProductDashboard.html',data)  

@login_required(login_url='nuevoLogin')
def updateProductDashboard(request,pk):
	shop = Shop.objects.get(owner=request.user)
	product = Product.objects.get(pk=pk)
	if request.POST:
		
		form = updateProductForm(request.POST,request.FILES,instance=product)
		
		if form.is_valid() is True:
			f = form.save(commit=False)
			f.shop = shop
			f.category_group = CategoryGroup.objects.get(pk=(int(request.POST['category_group'])))
			f.save()
			return redirect('menu')
		else:
			pass
	else:
		category_list = [ x.category_group for x in Product.objects.filter(shop = shop)]    
		html = None
		form = updateProductForm(instance=product)
		data = {
			"form":form,
			"category_list":category_list,
			"html":html,
		}
		return render(request,'updateProductDashboard.html',data)  


@login_required(login_url='nuevoLogin')
def viewProductDashboard(request,pk):
	product = Product.objects.get(pk=pk)
	html = None
	form = createProductForm()
	data = {
		"form":form,
		"product":product,
		"html":html,
	}
	return render(request,'viewProductDashboard.html',data)


@login_required(login_url='nuevoLogin')
def editarPlato(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'editarPlato.html',data)  

@login_required(login_url='nuevoLogin')
def editarExp(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'editarExp.html',data)    


@login_required(login_url='nuevoLogin')
def agregarNuevaExp(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'agregarNuevaExp.html',data)    


@login_required(login_url='nuevoLogin')
def promociones(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promociones.html',data)   


@login_required(login_url='nuevoLogin')
def tipoDePromocion(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'tipoDePromocion.html',data)  


@login_required(login_url='nuevoLogin')
def promocionPorPorcentaje(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promocionPorPorcentaje.html',data)  


@login_required(login_url='nuevoLogin')
def promocion2x1(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promocion2x1.html',data)  

@login_required(login_url='nuevoLogin')
def promocionEnvioGratis(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promocionEnvioGratis.html',data)  


@login_required(login_url='nuevoLogin')
def promocionAgregarPlatos(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promocionAgregarPlatos.html',data)  


@login_required(login_url='nuevoLogin')
def promocionAgregarAcom(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'promocionAgregarAcom.html',data)  


@login_required(login_url='nuevoLogin')
def editarPromocion(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'editarPromocion.html',data)  


@login_required(login_url='nuevoLogin')
def editarPromocionAgregarPlato(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'editarPromocionAgregarPlato.html',data)  

@login_required(login_url='nuevoLogin')
def editarPromocionAgregarAcom(request):
	

	html = None

	data = {
		
		"html":html,
	}
	return render(request,'editarPromocionAgregarAcom.html',data)  


@login_required(login_url='nuevoLogin')
def listUsersDashboard(request):

	shop = Shop.objects.get(owner=request.user)
	list_user_id = [x.user.id for x in UserShop.objects.filter(shop=shop)]
	list_user = User.objects.filter(pk__in=list_user_id)

	html = None

	data = {
		"list_user":list_user,
		"html":html,
	}
	return render(request,'listUsersDashboard.html',data)  


@login_required(login_url='nuevoLogin')
def createOperatorUsersDashboard(request):
	shop = Shop.objects.get(owner=request.user)
	if request.POST:
		
		if request.POST['password2'] == request.POST["password"]:
			form = createOperatorUsersForm(request.POST,request.FILES)
			if form.is_valid() is True:
				f = form.save(commit=False)
				f.username = f.email
				f.save()
				user = User.objects.get(email=request.POST['email'])
				UserShop.objects.create(user=user,shop=shop)
				user.set_password(f.password)
				user.save()
				return redirect('listUsersDashboard')
			else:
				pass
		else:
			form = createOperatorUsersForm()
			error = "Las contraseñas no coinciden"
			data = {
				"form":form,
				"error":error,
			}
			return render(request,'createOperatorUsersDashboard.html',data) 
	else:
		form = createOperatorUsersForm()
		data = {
			"form":form,
		}
		return render(request,'createOperatorUsersDashboard.html',data) 
		


@login_required(login_url='nuevoLogin')
def updateOperatorUsersDashboard(request,pk):
	shop = Shop.objects.get(owner=request.user)
	user = User.objects.get(pk = pk)
	if request.POST:
		form = updateOperatorUsersForm(request.POST,request.FILES,instance=user)
		if form.is_valid() is True:
			f = form.save(commit=False)
			f.username = f.email
			f.type_user = 3
			f.save()
			return redirect('listUsersDashboard')
		else:
			pass
		
	else:
		form = updateOperatorUsersForm(instance=user)
		data = {
			"form":form,
		}
		return render(request,'updateOperatorUsersDashboard.html',data) 

def addDeliveryUserDashboard(request):
	if request.POST:
		user_to_search = request.POST['delivery_user']
		
		if User.objects.filter(email=user_to_search,type_user=1).count() == 1:
			if UserShop.objects.filter(user=User.objects.get(email=user_to_search)).count() == 1:
				result = "error"
				msg = "Repartidor ya esta vinculado"
			else:
				msg = "Repartidor vinculado"
				result = "success"
				UserShop.objects.create(user=User.objects.get(email=user_to_search),shop=Shop.objects.get(owner=request.user))

		else:
			msg = "No se encuentra un repartidor con este email"
			result = "error"

		data = {
			"result":result,
			"msg":msg,
		}
		return render(request,'addDeliveryUserDashboard.html',data) 
	else:
		data = {

		}
		return render(request,'addDeliveryUserDashboard.html',data) 


def nuevoLogin(request):
	
	hidden_navbar = True

	if request.user.is_authenticated:
		return redirect('home')
	else:
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
				if user is not None:
					try:
						if user.is_active:
							login(request, user)
							return redirect('home')
					except:
						login_form = LoginForm()
						dataErrorLogin = "Lo sentimos, su usuario no esta habilitado para ingresar al sistema"
						return render(request, 'nuevoLogin.html', {'login_form': login_form,"hidden_navbar":hidden_navbar, 'dataErrorLogin': dataErrorLogin})
				else:
					login_form = LoginForm()
					dataErrorLogin = "Usuario y/o contraseña no son válidos"
					return render(request, 'nuevoLogin.html', {'login_form': login_form,"hidden_navbar":hidden_navbar, 'dataErrorLogin': dataErrorLogin})
			else:
				raise ('Error Login : Form Invalid')
		else:
			login_form = LoginForm()
			return render(request, 'nuevoLogin.html', {'login_form': login_form,"hidden_navbar":hidden_navbar,})
   
	


def nuevoRegistro(request):
	

	html = None
	hidden_navbar = True

	data = {
		
		"html":html,
		"hidden_navbar":hidden_navbar,
	}
	return render(request,'nuevoRegistro.html',data)      


def recuperarContraseña(request):
	

	html = None
	hidden_navbar = True

	data = {
		
		"html":html,
		"hidden_navbar":hidden_navbar,
	}
	return render(request,'recuperarContraseña.html',data)   


def restaurarContraseña(request):
	

	html = None
	hidden_navbar = True

	data = {
		
		"html":html,
		"hidden_navbar":hidden_navbar,
	}
	return render(request,'restaurarContraseña.html',data)   


