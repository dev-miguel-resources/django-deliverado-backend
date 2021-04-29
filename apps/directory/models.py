from django.db import models
from apps.users.models import User, AddressUser



class Experience(models.Model):
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to="experiences")
	size_list = models.IntegerField(default=0)
	img_cover = models.ImageField(upload_to="experiences")

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to="category")
	size_list = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Shop(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	img_list = models.ImageField(upload_to="shop_list",blank=True)
	img_cover = models.ImageField(upload_to="shop_cover",blank=True)
	description = models.CharField(max_length=150,blank=True)
	category = models.IntegerField(default=0)
	status = models.IntegerField(default=0)

	lat = models.CharField(max_length=150,blank=True)
	lng = models.CharField(max_length=150,blank=True)
	
	address = models.CharField(max_length=150,blank=True)
	phone = models.CharField(max_length=150,blank=True)
	email = models.EmailField(max_length=150,blank=True)

	hours_week_start = models.IntegerField(default=0)
	hours_week_end = models.IntegerField(default=0)
	hours_sat_start = models.IntegerField(default=0)
	hours_sat_end = models.IntegerField(default=0)
	hours_sun_start = models.IntegerField(default=0)
	hours_sun_end = models.IntegerField(default=0)

	


	

	type_business_list = (
		('general','general'), 
		('mexicana','mexicana')
	)	
	type_business = models.CharField(max_length=50,choices=type_business_list,default="general")

	def __str__(self):
		return self.name

class TypeProduct(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class CategoryGroup(models.Model):
	name = models.CharField(max_length=50)
	shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class ExperienceGroup(models.Model):
	name = models.CharField(max_length=50)
	shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class Product(models.Model):
	shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to='products',null=True,blank=True)
	description = models.CharField(max_length=150)
	price = models.IntegerField(default=100)
	category_home = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
	category_group = models.ForeignKey("CategoryGroup", on_delete=models.CASCADE)
	status = models.IntegerField(default=1)

class FeaturedProduct(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

class PromotionShop(models.Model):
	shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
	img = models.ImageField(upload_to="shop_promotions")
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=150)
	value = models.IntegerField(default=0)
	type_promotion = models.IntegerField(default=0)
	date_start = models.DateTimeField()
	date_finish = models.DateTimeField()

class ExperienceProduct(models.Model):
	experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

class CategoryProduct(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

class FeaturedShop(models.Model):
	shop = models.ForeignKey(Shop,on_delete=models.CASCADE)


class Order(models.Model):
	# - 0 In progress 
	# - 1 Waiting confirmation 
	# - 2 shop confirmation 
	# - 3 shop reject  
	# - 4 delivery confirmation 
	# - 5 delivery cancel 
	# - 6 in preparation 
	# - 7 in route to pick 
	# - 8 in route to delivery 
	# - 9 delivery ok

	
	shop =  models.ForeignKey(Shop,on_delete=models.CASCADE)
	user_customer = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_customer")
	user_delivery = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_delivery", null=True, blank= True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_to_delivery = models.DateTimeField(blank=True,null=True)
	status = models.IntegerField(default=0) 
	total = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	delivery_tax = models.IntegerField(default=0)
	address_delivery = models.ForeignKey(AddressUser,on_delete=models.CASCADE,null=True,blank=True)
	cooking_time = models.IntegerField(default=0)

class OrderHistoryStatus(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	status = models.IntegerField(default=0) 
	date = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	sub_total = models.IntegerField()

class FeedbackOrder(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	type_feedback = models.IntegerField(default=0)
	value = models.IntegerField(default=1)
	date_created = models.DateTimeField(auto_now_add=True)
	order = models.ForeignKey(Order,on_delete=models.CASCADE)

class MessageOrder(models.Model):
	from_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="from_user")
	to_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="to_user")
	message = models.CharField(max_length=150)
	date_created = models.DateTimeField(auto_now_add=True)
	order = models.ForeignKey(Order,on_delete=models.CASCADE)


class ReportOrder(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user")
	type_report = models.IntegerField(default=0)
	details = models.CharField(max_length=300)

class DataGPS(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	lat = models.CharField(max_length=300)
	lng = models.CharField(max_length=300)
	date_created = models.DateTimeField(auto_now_add=True)


class UserShop(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	type_user = models.IntegerField(default=0) # 0 - operador / 1 - repartidor
	shop = models.ForeignKey(Shop,on_delete=models.CASCADE)