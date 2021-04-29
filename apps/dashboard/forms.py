from django import forms
from apps.users.models import *
from apps.directory.models import *


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,
	   widget=forms.TextInput(attrs={
		   'class': 'form-control',
		   'placeholder':"Ingresa tu Correo",
		   'required': 'true',
	   }))
	password = forms.CharField(max_length=30,
	   widget=forms.TextInput(attrs={
		   'type': 'password',
		   'class': 'form-control',
		   'placeholder':"Ingresa tu Clave",
		   'required': 'true'
	   }))

class RegisterForm(forms.Form):
	email = forms.CharField(max_length=30,
	   widget=forms.TextInput(attrs={
		   'class': 'form-control',
		   'placeholder':"Ingresa tu Correo",
		   'required': 'true',
	   }))
	password = forms.CharField(max_length=30,
	   widget=forms.TextInput(attrs={
		   'type': 'password',
		   'class': 'form-control',
		   'placeholder':"Ingresa tu Clave",
		   'required': 'true'
	   }))
	phone = forms.CharField(max_length=30,
	   widget=forms.TextInput(attrs={
		   'type': 'text',
		   'class': 'form-control',
		   'placeholder':"Ingresa tu Télefono",
		   'required': 'true'
	   }))


class updateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name', 'email','type_user')
		widgets = {
			'first_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'last_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			 'type_user': forms.Select(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
 
		}


class createProductForm(forms.ModelForm):
	# def __init__(self,shop, **kwargs):
	# 	super(createProductForm, self).__init__(**kwargs)
		
	# 	self.fields['category_group'].queryset = CategoryGroup.objects.filter(shop=shop)

	class Meta:
		
		model = Product
		fields = ('name','img','description','price','category_group')
		widgets = {
		 

			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			 'img': forms.FileInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'description': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			  'price': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			  'category_group': forms.Select(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
 
			
 

 
		}

class updateProductForm(forms.ModelForm):
    	# def __init__(self,shop, **kwargs):
	# 	super(createProductForm, self).__init__(**kwargs)
		
	# 	self.fields['category_group'].queryset = CategoryGroup.objects.filter(shop=shop)

	class Meta:
		
		model = Product
		fields = ('name','img','description','price','category_group')
		widgets = {
		 

			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			 'img': forms.FileInput(attrs={
				'class': 'form-control',

			}),
			 'description': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			  'price': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			  'category_group': forms.Select(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
 
			
 

 
		}

class createOperatorUsersForm(forms.ModelForm):
	# def __init__(self,shop, **kwargs):
	# 	super(createProductForm, self).__init__(**kwargs)
		
	# 	self.fields['category_group'].queryset = CategoryGroup.objects.filter(shop=shop)

	class Meta:
		
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password',
			'manage_order',
			'manage_promo',
			'manage_menu',
			'manage_profile',
		)
		widgets = {
		
			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			 'first_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'last_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'password': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'manage_order': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_promo': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_menu': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_profile': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
	 
		}

class updateOperatorUsersForm(forms.ModelForm):
	# def __init__(self,shop, **kwargs):
	# 	super(createProductForm, self).__init__(**kwargs)
		
	# 	self.fields['category_group'].queryset = CategoryGroup.objects.filter(shop=shop)

	class Meta:
		
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'manage_order',
			'manage_promo',
			'manage_menu',
			'manage_profile',
			 
		)
		widgets = {
		
			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

			 'first_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'last_name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),
			 'manage_order': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_promo': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_menu': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 'manage_profile': forms.CheckboxInput(attrs={
				'class': 'form-control',
				
			}),
			 
	 
		}

class updateProfileShopForm(forms.ModelForm):
    	# def __init__(self,shop, **kwargs):
	# 	super(createProductForm, self).__init__(**kwargs)
		
	# 	self.fields['category_group'].queryset = CategoryGroup.objects.filter(shop=shop)

	class Meta:
		
		model = Shop
		fields = (
			'email',

			'address',
			'type_business',
			'phone',

			'hours_week_start',
			'hours_week_end',
			'hours_sat_start',
			'hours_sat_end',
			'hours_sun_start',
			'hours_sun_end',
			
			 
		)
		widgets = {
		
			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'required': 'true'
			}),

		 
			 'type_business': forms.Select(attrs={
				'class': 'form-control',
				'required': 'true',
			 
			}),
			 'address': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true',
			 
			}),
			 'phone': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true',
			 
			}),



			'hours_week_start': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				
			}),
			'hours_week_end': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				
			}),
			'hours_sat_start': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				

			}),
			'hours_sat_end': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				

			}),
			'hours_sun_start': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				
			}),
			'hours_sun_end': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true',
				'min':'1',
				'max':'24',
				
			}),
			 
	 
		}
