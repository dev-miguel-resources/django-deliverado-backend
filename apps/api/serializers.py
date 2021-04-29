#general
from rest_framework.serializers import  *
from rest_framework.serializers import  ModelSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueTogetherValidator
from datetime import date
import random	
from drf_extra_fields.fields import Base64ImageField

#models
from apps.users.models import *
from apps.directory.models import *

#
from django.core.mail import send_mail, EmailMessage
from django.conf import settings



#########################################
##  SERIALIZERS MODULE USERS           ## 
#########################################

class UserSerializer(ModelSerializer):
	antecedentes_front  = Base64ImageField()  
	antecedentes_back  = Base64ImageField()  
	avatar  = Base64ImageField()  
	class Meta:		 
		model = User 
		fields = (
			'pk',
			'email',
			'avatar',
			'first_name',
			'last_name',
			'join_date',
			'type_user',
			'phone',
			'validated_phone',
			'is_active',
			'is_staff',
			'antecedentes_front',
			'antecedentes_back',
			'driver_active',

		)

		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['email','phone'],
				message="Email y/o Teléfono ya registrados",
			)
		]


	def create(self, validated_data):
		if User.objects.filter(email=validated_data['email']).count() != 0:
			pass
		else:
			'''# Download the helper library from https://www.twilio.com/docs/python/install
			from twilio.rest import Client


			# Your Account Sid and Auth Token from twilio.com/console
			# DANGER! This is insecure. See http://twil.io/secure
			account_sid = 'AC64ac52ea85693b3e02dd875a670b1a9e'
			auth_token = 'ae4512f40208275de2351358461530e1'
			client = Client(account_sid, auth_token)

			message = client.messages \
							.create(
								from_='whatsapp:+14155238886',
								body='Your appointment is coming up on July 21 at 3PM',
								to='whatsapp:+56988955561'
							)

			print(message.sid)
			'''

			random_password = random.randint(111111111, 9999999999999)
			user = User(
				email=validated_data['email'],
				username=validated_data['email'],
				first_name=validated_data['first_name'],
				last_name=validated_data['last_name'],
				phone = validated_data['phone'],
				type_user = validated_data['type_user'],
				antecedentes_back = validated_data['antecedentes_back'],
				antecedentes_front = validated_data['antecedentes_front'],
				
			)
			user.set_password(random_password)
			user.save()

			return user

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email',instance.email)
		instance.username = validated_data.get('email',instance.username)
		instance.first_name = validated_data.get('first_name',instance.first_name)
		instance.last_name = validated_data.get('last_name',instance.last_name)
		instance.phone = validated_data.get('phone',instance.phone)
		instance.antecedentes_back = validated_data.get('antecedentes_back',instance.antecedentes_back)
		instance.antecedentes_front = validated_data.get('antecedentes_front',instance.antecedentes_front)

		instance.avatar = validated_data.get('avatar',instance.avatar)
		 
		instance.save()
		return instance



class UserNoAvatarSerializer(ModelSerializer):
	antecedentes_front  = Base64ImageField()  
	antecedentes_back  = Base64ImageField()  
 
	class Meta:		 
		model = User 
		fields = (
			'pk',
			'email',
			
			'first_name',
			'last_name',
			'join_date',
			'type_user',
			'phone',
			'validated_phone',
			'is_active',
			'is_staff',
			'antecedentes_front',
			'antecedentes_back',

		)

		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['email','phone'],
				message="Email y/o Teléfono ya registrados",
			)
		]


	def create(self, validated_data):
		if User.objects.filter(email=validated_data['email']).count() != 0:
			pass
		else:
			'''# Download the helper library from https://www.twilio.com/docs/python/install
			from twilio.rest import Client


			# Your Account Sid and Auth Token from twilio.com/console
			# DANGER! This is insecure. See http://twil.io/secure
			account_sid = 'AC64ac52ea85693b3e02dd875a670b1a9e'
			auth_token = 'ae4512f40208275de2351358461530e1'
			client = Client(account_sid, auth_token)

			message = client.messages \
							.create(
								from_='whatsapp:+14155238886',
								body='Your appointment is coming up on July 21 at 3PM',
								to='whatsapp:+56988955561'
							)

			print(message.sid)
			'''

			random_password = random.randint(111111111, 9999999999999)
			user = User(
				email=validated_data['email'],
				username=validated_data['email'],
				first_name=validated_data['first_name'],
				last_name=validated_data['last_name'],
				phone = validated_data['phone'],
				type_user = validated_data['type_user'],
				antecedentes_back = validated_data['antecedentes_back'],
				antecedentes_front = validated_data['antecedentes_front'],
				
			)
			user.set_password(random_password)
			user.save()

			return user

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email',instance.email)
		instance.username = validated_data.get('email',instance.username)
		instance.first_name = validated_data.get('first_name',instance.first_name)
		instance.last_name = validated_data.get('last_name',instance.last_name)
		instance.phone = validated_data.get('phone',instance.phone)
		instance.antecedentes_back = validated_data.get('antecedentes_back',instance.antecedentes_back)
		instance.antecedentes_front = validated_data.get('antecedentes_front',instance.antecedentes_front)


		 
		instance.save()
		return instance


class AddressUserSerializer(ModelSerializer):
	class Meta:		 
		model = AddressUser
		fields = (
			'pk',
			'user',
			'is_primary',
			'address_1',
			'address_2',
			'lat',
			'lng',
			'notes',
		)



class ExperienceSerializer(ModelSerializer):
	class Meta:
		model = Experience
		fields = ( 
			'pk',
			'name',
			'img',
			'size_list',
			'img_cover',
		)
class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = ( 
			'pk',
			'name',
			'img',
			'size_list',
		)
class ShopSerializer(ModelSerializer):
	class Meta:
		model = Shop
		fields = ( 
			'pk',
			'owner',
			'name',
			'img_list',
			'img_cover',
			'description',
			'category',
			'status',
			'lat',
			'lng',
		)



class TypeProductSerializer(ModelSerializer):
	class Meta:
		model = TypeProduct
		fields = (
			'name',
		)	



class ProductSerializer(ModelSerializer):
	shop = ShopSerializer(read_only=True)
	class Meta:
		model = Product
		fields = ( 
			'pk',
			'shop',
			'name',
			'img',
			'description',
			'price',
			# 'category_group',
		)

class FeaturedProductSerializer(ModelSerializer):
	product = ProductSerializer(read_only=True)
	class Meta:
		model = FeaturedProduct
		fields = ( 
			'pk',
			'product',
		)

class PromotionShopSerializer(ModelSerializer):
	shop = ShopSerializer(read_only=True)
	class Meta:
		model = PromotionShop
		fields = ( 
			'pk',
			'shop',
			'img',
			'title',
			'description',
			'value',
			'type_promotion',
			'date_start',
			'date_finish',
		)

class ExperienceProductSerializer(ModelSerializer):
	product = ProductSerializer(read_only=True)
	class Meta:
		model = ExperienceProduct
		fields = ( 
			'pk',
			'experience',
			'product',
		)
class CategoryProductSerializer(ModelSerializer):
	product = ProductSerializer(read_only=True)
	class Meta:
		model = CategoryProduct
		fields = ( 
			'pk',
			'category',
			'product',
		)
class FeaturedShopSerializer(ModelSerializer):
	shop = ShopSerializer(read_only=True)
	class Meta:
		model = FeaturedShop
		fields = ( 
			'pk',
			'shop'
		)


class OrderSerializer(ModelSerializer):
	user_delivery = UserSerializer(read_only=True)
	user_customer = UserSerializer(read_only=True)
	shop = ShopSerializer(read_only=True)
	address_delivery = AddressUserSerializer(read_only=True)
	
	class Meta:
		model = Order
		fields = ( 
			'pk',
			'shop',
			'user_customer',
			'user_delivery',
			'date_created',
			'date_to_delivery',
			'status',
			'quantity',
			'total',
			'delivery_tax',
			'address_delivery',
		)

class OrderHistoryStatusSerializer(ModelSerializer):
		class Meta:
			model = OrderHistoryStatus
			fields = ( 
				'order',
				'status',
				'date'
			)

class OrderProductSerializer(ModelSerializer):
	product = ProductSerializer(read_only=True)
	class Meta:
		model = OrderProduct
		fields = ( 
			'pk',
			'order',
			'product',
			'quantity',
			'sub_total',
		)

class AddOrderProductSerializer(ModelSerializer):
	class Meta:
		model = OrderProduct
		fields = ( 
			'order',
			'product',
			'quantity',
			'sub_total',
		)


class MessageOrderSerializer(ModelSerializer):
	from_user = UserSerializer(read_only=True)
	to_user = UserSerializer(read_only=True)
	class Meta:
		model = MessageOrder
		fields = ( 
			'from_user',
			'to_user',
			'message',
			'date_created',
			'order',
		)

class AddMessageOrderSerializer(ModelSerializer):
	class Meta:
		model = MessageOrder
		fields = ( 
			'from_user',
			'to_user',
			'message',
			'date_created',
			'order',
		)

class FeedbackOrderSerializer(ModelSerializer):
		class Meta:
			model = FeedbackOrder
			fields = ( 
				'user',
				'type_feedback',
				'value',
				'date_created',
				'order',
			)


class ReportOrderSerializer(ModelSerializer):
	class Meta:
		model = ReportOrder
		fields = ( 
			'order',
			'date_created',
			'user',
			'type_report',
			'details',
		)



class VehicleSerializer(ModelSerializer):
	license_front  = Base64ImageField()  
	license_back = Base64ImageField()  
	document_vehicle_1 = Base64ImageField()  
	document_vehicle_2 = Base64ImageField()  

	class Meta:
		model = Vehicle
		fields = ( 
			'user',
			'type_vehicle',
			'serie',
			'model_vehicle',
			'license_front',
			'license_back',
			'document_vehicle_1',
			'document_vehicle_2',
		)


class DataGPSSerializer(ModelSerializer):
	  

	class Meta:
		model = DataGPS
		fields = ( 
			'user',
			'lat',
			'lng',
			 
		)



class CategoryGroupSerializer(ModelSerializer):
		class Meta:
			model = CategoryGroup
			fields = (
				'pk',
				'name',
				'shop',
			)	


	

 




