#/general
from apps.api.serializers import *
from django.db.models import Q
from datetime import date, timedelta
from django.http import HttpResponse, JsonResponse
import requests
from django.db.models import Sum,Min
from django.db.models.functions import Lower
import random	
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import get_object_or_404

#drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token

# others
import os
from twilio.rest import Client

#models
from apps.users.models import *
from apps.directory.models import *
from apps.drp.views import *


#####################################
##  VIEWS MODULE USERS            ## 
#####################################

class CurrentUserView(APIView):
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)

class reset_password(APIView):
	permission_classes = (AllowAny,)
	def post(self, request, *args, **kwargs):
		user = User.objects.get(email=self.request.data['email'])
		new_token(user.pk)
		status = {"code":"send email"}
		return Response(status)

class UserCreate(generics.CreateAPIView):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetailNoAvatar(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserNoAvatarSerializer


class LoginMobile(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		number = "+569" + str(request.data["number"])
		type_send = request.data["type_send"]
		msj = "error"
		new_code = random.randint(1111, 9999)
		PhoneCode.objects.create(phone=request.data["number"],code=new_code,type_code=0)
		
		if type_send == 1 or type_send == "1":
			print (new_code)
			

			# account_sid = "AC39204a4c2d7df8e5fc57493bf830f70f"
			# auth_token = "8b83e4c7f216be09fa63f87ee5abdf78"
			# number_deliverado = "+16026413017"

			#temporadal de getgo
			account_sid = "AC02b13fe6a4485649c559db1f5343aba9"
			auth_token = "d1b4689bf7c1846be65340b4e65a9632"

			number_deliverado = "+12072451291"
			
			client = Client(account_sid, auth_token)

			message = client.messages \
				.create(
					 body='Tu Código de validación Deliverado-Repartidor es: ' + str(new_code),
					 from_= str(number_deliverado),
					 to = str(number)
					 
				 )

		else:
			


			# Your Account Sid and Auth Token from twilio.com/console
			# and set the environment variables. See http://twil.io/secure
			# account_sid = "AC39204a4c2d7df8e5fc57493bf830f70f"
			# auth_token = "8b83e4c7f216be09fa63f87ee5abdf78"
			# number_deliverado = "+16026413017"

			#temporadal de getgo
			account_sid = "AC02b13fe6a4485649c559db1f5343aba9"
			auth_token = "d1b4689bf7c1846be65340b4e65a9632"

			number_deliverado = "+12072451291"

			client = Client(account_sid, auth_token)

			message = client.messages.create(
										from_='whatsapp:'+str(number_deliverado),
										body=str(new_code),
										to='whatsapp:' + str(number)
									)

			print(message.sid)



		# msg = "El Código es: " + str(new_code)
		# email = EmailMessage('Nuevo Codigo Deliverado', msg , to=['testingdeliverado@mailinator.com'])
		# email.content_subtype = 'html'
		# email.send()			
		data = {
			"msj":msj,
		}
		return JsonResponse(data)

class MyToken(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		# import pdb; pdb.set_trace()
		number = request.data["phone"]
		user = User.objects.get(phone = number)
		get_token = Token.objects.get_or_create(user=user)[0]
		from django.http import JsonResponse
		from django.forms.models import model_to_dict
		token = model_to_dict(get_token)["key"]
		data = {
				"token" : token
			}
		return JsonResponse(data)
		

class HasVehicleView(APIView):
	def get(self, request):
		if Vehicle.objects.filter(user=request.user).count() > 0:
			response = "true"
		else:
			response = "false"

		data = {
				"response" : response
			}
		return JsonResponse(data)	

		
				


class ValidateCode(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		number = request.data["number"]
		code = request.data["code"]
		msj = "error"
		
		if PhoneCode.objects.filter(phone=number,code=code).count() == 1:
			User.objects.filter(phone=number).update(validated_phone=True)
			
			if User.objects.filter(phone=number).count() > 0:
				# hay que mandarlo al home
				msj = "login" 
			else:
				#hay que registrar al usuario
				msj = "register" 
			
			PhoneCode.objects.filter(phone=number,code=code).update(is_used=True)
		
		
		else:
			msj = "error"
		
		data = {
			"msj":msj,
		}
		return JsonResponse(data)

class RequestChangePassword(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		to_send = request.data["to_send"]
		type_request = request.data["type_request"]
		userid = ''
		
		if type_request ==  '0':
			user = User.objects.get(email=to_send)
		elif type_request ==  '1':
			user = User.objects.get(phone=to_send)
		
		try:
			#aca se genera 
			new_code = random.randint(1111, 9999)
			PhoneCode.objects.create(user=user,code=new_code,type_code=1)

			#aca se envia el código 
			
			if type_request == '0':
				msg = "El Código es: " + str(new_code)
				email = EmailMessage('Reset Password Deliverado', msg , to=[to_send])
				email.content_subtype = 'html'
				email.send()
				
			
			msj = "send"
			userid = user.pk
			

		except:
			msj = "error"

		data = {
			"msj":msj,
			"userid":userid
		}

		
		return JsonResponse(data)

class ChangePassword(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		user = request.data["user"]
		new_password = request.data["new_password"]

		user = User.objects.filter(pk=user)[0]
		user.set_password(new_password)
		user.save()

		msj = "ok"
		
		data = {
			"msj":msj,
		}
		
		return JsonResponse(data)

class ValidateQR(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		user_delivery = request.data["user_delivery"]
		user_customer = request.data["user_customer"]
		order = request.data["order"]
		
		
		msj = "error"
		if Order.objects.filter(user_customer=user_customer,user_delivery=user_delivery,pk=order).count() == 1:
			Order.objects.filter(user_customer=user_customer,user_delivery=user_delivery,pk=order).update(status=9)
			msj = "complete"
		else:
			msj = "error"

		data = {
			"msj":msj,
		}
		return JsonResponse(data)


class AddressUserList(generics.ListCreateAPIView):
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user']
	queryset = AddressUser.objects.all()
	serializer_class = AddressUserSerializer


class AddressUserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = AddressUser.objects.all()
	serializer_class = AddressUserSerializer

	def put(self,request,*args, **kwargs):
		address = AddressUser.objects.filter(pk=kwargs["pk"],user=request.user).update(is_primary=True)
		AddressUser.objects.filter(user=request.user).exclude(pk=kwargs["pk"]).update(is_primary=False)
		serializer = AddressUserSerializer(address,data = request.data)
		data = {
			"status":"ok",
		}
		return JsonResponse(data)
 
class ExperienceList(generics.ListCreateAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer
 

class CategoryList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ShopList(generics.ListCreateAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Shop.objects.all()
	serializer_class = ShopSerializer


class ShopSearch(generics.ListAPIView):
	serializer_class = ShopSerializer
	def get_queryset(self):
		word = self.request.GET["word"].strip()
		word  = word.lower()
		import time
		# time.sleep(2)
		return Shop.objects.filter(name__contains=word) | Shop.objects.filter(name__startswith=word) | Shop.objects.filter(description__contains=word) 

class ListCategoryShop(generics.ListAPIView):
	serializer_class = ShopSerializer
	def get_queryset(self):
    		
		import pdb; pdb.set_trace()
		
		product_list = Product.objects.values('category_home').annotate(pk=Min('pk'))
		
		shopList = [x.shop for x in product_list]

		return shopList



class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['shop','category_group']
	serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class FeaturedProductList(generics.ListCreateAPIView):
	queryset = FeaturedProduct.objects.all()
	serializer_class = FeaturedProductSerializer


class FeaturedProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = FeaturedProduct.objects.all()
	serializer_class = FeaturedProductSerializer



class PromotionShopList(generics.ListCreateAPIView):
	queryset = PromotionShop.objects.all()
	serializer_class = PromotionShopSerializer


class PromotionShopDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PromotionShop.objects.all()
	serializer_class = PromotionShopSerializer


class ExperienceProductList(generics.ListCreateAPIView):
	queryset = ExperienceProduct.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['experience']
	serializer_class = ExperienceProductSerializer


class ExperienceProductDetail(generics.RetrieveUpdateDestroyAPIView):  
	queryset = ExperienceProduct.objects.all()
	serializer_class = ExperienceProductSerializer


class CategoryProductList(generics.ListCreateAPIView):
	queryset = CategoryProduct.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['category']
	serializer_class = CategoryProductSerializer


class CategoryProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CategoryProduct.objects.all()
	serializer_class = CategoryProductSerializer


class FeaturedShopList(generics.ListCreateAPIView):
	queryset = FeaturedShop.objects.all()
	serializer_class = FeaturedShopSerializer


class FeaturedShopDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = FeaturedShop.objects.all()
	serializer_class = FeaturedShopSerializer



class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user_delivery','user_customer','status']
	serializer_class = OrderSerializer


class OrderFilterDates(generics.ListAPIView):
	# queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		
		date1 = self.request.GET["date1"]
		date2 = self.request.GET["date2"]
		user = self.request.GET["user"]
		orders = Order.objects.filter(user_delivery=user, date_to_delivery__lte=date2,date_to_delivery__gte=date1)
		return  orders


class OrderAddressDetail(generics.RetrieveUpdateDestroyAPIView):
	# queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		
		user = Order.objects.get(pk=self.kwargs["pk"]).user_customer.pk
		address_primary = AddressUser.objects.get(user=user,is_primary=True)
		Order.objects.filter(pk=self.kwargs["pk"]).update(address_delivery=address_primary)

		order_id = self.kwargs["pk"]

		return Order.objects.filter(pk=order_id)
		

		
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def put(self,request,*args, **kwargs):
		order = Order.objects.get(pk=kwargs["pk"])
		
		# if not request.data["user_delivery"] == None:
		# 	user_delivery = User.objects.get(pk=request.data["user_delivery"])

		serializer = OrderSerializer(order,data = request.data)
		
		if serializer.is_valid():
			serializer.save()
		
		# if not request.data["user_delivery"] == None:
		# 	Order.objects.filter(pk=kwargs["pk"]).update(user_delivery = User.objects.get(pk=request.data["user_delivery"]))
		if not request.data["status"] == None:
			OrderHistoryStatus.objects.create(order=order,status=request.data["status"])

			
		return Response(serializer.data)  

class OrderAddDriverDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def put(self,request,*args, **kwargs):
		order = Order.objects.get(pk=kwargs["pk"])
		
		if not request.data["user_delivery"] == None:
			user_delivery = User.objects.get(pk=request.data["user_delivery"])

		serializer = OrderSerializer(order,data = request.data)
		
		if serializer.is_valid():
			serializer.save()
		
		# if not request.data["user_delivery"] == None:
		Order.objects.filter(pk=kwargs["pk"]).update(user_delivery = User.objects.get(pk=request.data["user_delivery"]))
		if not request.data["status"] == None:
			OrderHistoryStatus.objects.create(order=order,status=request.data["status"])

			
		return Response(serializer.data)  

class OrderHistoryStatusList(generics.ListCreateAPIView):
	queryset = OrderHistoryStatus.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['order']
	serializer_class = OrderHistoryStatusSerializer


class OrderHistoryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OrderHistoryStatus.objects.all()
	serializer_class = OrderHistoryStatusSerializer		



class OrderProductList(generics.ListCreateAPIView):
	queryset = OrderProduct.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['order']
	serializer_class = OrderProductSerializer

	
class AddOrderProductList(generics.ListCreateAPIView):
	#queryset = OrderProduct.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['order']
	#serializer_class = AddOrderProductSerializer
	def post(self,request):

		order = Order.objects.get(pk=request.data["order"])
		product = Product.objects.get(pk=request.data["product"])
		quantity = request.data["quantity"]
		sub_total = request.data["sub_total"]
		

		if OrderProduct.objects.filter(order=order,product=product).count() > 0:
			query = OrderProduct.objects.get(order=order,product=product)

			new_quantity_product = query.quantity + quantity
			sub_total = new_quantity_product * product.price
			OrderProduct.objects.filter(order=order,product=product).update(quantity=new_quantity_product,sub_total=sub_total)


			
			total = OrderProduct.objects.filter(order=order).aggregate(Sum('sub_total'))
			quantity = OrderProduct.objects.filter(order=order).aggregate(Sum('quantity'))
			Order.objects.filter(pk=order.pk).update(total=total["sub_total__sum"],quantity=quantity["quantity__sum"])

			
			serializer = AddOrderProductSerializer(query)
		else:
			query = OrderProduct.objects.create(order=order,product=product,quantity=quantity,sub_total=sub_total)
			serializer = AddOrderProductSerializer(query)

		return Response(serializer.data)



class OrderProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = OrderProduct.objects.all()
	serializer_class = OrderProductSerializer


class MessageOrderList(generics.ListCreateAPIView):
	queryset = MessageOrder.objects.all()
	serializer_class = MessageOrderSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['order']


class AddMessageOrderList(generics.ListCreateAPIView):
	queryset = MessageOrder.objects.all()
	serializer_class = AddMessageOrderSerializer

	
class MessageOrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MessageOrder.objects.all()
	serializer_class = MessageOrderSerializer





class FeedbackOrderList(generics.ListCreateAPIView):
	queryset = FeedbackOrder.objects.all()
	serializer_class = FeedbackOrderSerializer


class FeedbackOrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = FeedbackOrder.objects.all()
	serializer_class = FeedbackOrderSerializer


class ReportOrderList(generics.ListCreateAPIView):
	queryset = ReportOrder.objects.all()
	serializer_class = ReportOrderSerializer


class ReportOrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ReportOrder.objects.all()
	serializer_class = ReportOrderSerializer


class VehicleList(generics.ListCreateAPIView):
	queryset = Vehicle.objects.all()
	serializer_class = VehicleSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user']
	
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Vehicle.objects.all()
	serializer_class = VehicleSerializer


class GetLastOrder(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		user = request.data["user"]
		shop = request.data["shop"]


		shop = Shop.objects.get(pk=shop)
		user = User.objects.get(pk=user)

		address_primary = AddressUser.objects.get(user=user,is_primary=True)
		
		if Order.objects.filter(user_customer=user).exclude(status__in=(1,2,7)).count() > 0:
			order = Order.objects.filter(user_customer=user).exclude(status__in=(1,2,7)).latest('id')
		else:
			order = Order.objects.create(shop = shop, user_customer = user, address_delivery=address_primary)
	  
		serializer = OrderSerializer(order)
		return Response(serializer.data)


class GetCartOrder(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		user = request.data["user"]
		user = User.objects.get(pk=user)
 
		if Order.objects.filter(user_customer=user).exclude(status__in=(1,2,7)).count() > 0:
			order = Order.objects.filter(user_customer=user).exclude(status__in=(1,2,7)).latest('id')
		 
	  
		serializer = OrderSerializer(order)
		return Response(serializer.data)

class GetDistanceTime(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		url = request.data["api"]
		import requests
		value_km = 500
		response = requests.get(url).json()
		res = response["rows"][0]["elements"][0]["distance"]["value"]
		value_delivery = round(res * value_km/1000)
		data = {
			"valor":value_delivery,
			"km":response["rows"][0]["elements"][0]["distance"]["text"]
		}
		return JsonResponse(data)


class DataGPSList(generics.ListCreateAPIView):
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['user']
	queryset = DataGPS.objects.all().order_by("-id")
	serializer_class = DataGPSSerializer


class DataGPSDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DataGPS.objects.all()
	serializer_class = DataGPSSerializer

class CategoryGroupList(generics.ListCreateAPIView):
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['shop','name']
	queryset = CategoryGroup.objects.all().order_by("-id")
	serializer_class = CategoryGroupSerializer


class CategoryGroupDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CategoryGroup.objects.all()
	serializer_class = CategoryGroupSerializer


 