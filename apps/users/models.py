from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            pass
            # raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                                 True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    #general
    username = models.CharField(max_length=100, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField()
    is_validated = models.BooleanField(default=False)

    #personal
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)

    #extras
    avatar = models.ImageField(upload_to="avatar",blank=True)
    type_login = models.IntegerField(default=0) # 0 correo / 1 Facebook / 2 Gmail
    type_user = models.IntegerField(default=0) # 0 cliente / 1 Repartidor / 2 restaurant / 3 - operador / 999 admin
    phone = models.IntegerField(default=00000000000)
    validated_phone = models.BooleanField(default=False)
    
    
    #solo operator
    manage_order = models.BooleanField(default=False)
    manage_promo = models.BooleanField(default=False)
    manage_menu = models.BooleanField(default=False)
    manage_profile = models.BooleanField(default=False)
    
    #solo conductor
    driver_active = models.BooleanField(default=False)
    antecedentes_front = models.ImageField(upload_to="antecedentes_front",blank=True,null=True)
    antecedentes_back = models.ImageField(upload_to="antecedentes_back",blank=True,null=True)

    


    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def get_short_name(self):
        return self.username

class PhoneCode(models.Model):
    phone = models.IntegerField(default=00000000000)
    code = models.IntegerField(default=0000)
    type_code = models.IntegerField(default=0) # 0 verification  - 1 reset password
    is_used = models.BooleanField(default=False)


class AddressUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    address_1 = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    lat = models.CharField(max_length=300,blank=True)
    lng = models.CharField(max_length=300,blank=True)
    notes = models.CharField(max_length=140,blank=True)

    def __str__(self):
        return self.address_1 +' '+self.address_2
    

class Vehicle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type_vehicle = models.IntegerField(default=0) # 0 auto - 1 moto - 2 bici
    serie = models.CharField(max_length = 100 )
    model_vehicle = models.CharField(max_length = 100, blank=True )
    license_front = models.ImageField(upload_to="license_front",null=True)
    license_back  = models.ImageField(upload_to="license_back",null=True)
    document_vehicle_1 = models.ImageField(upload_to="document_vehicle_1",null=True)
    document_vehicle_2 = models.ImageField(upload_to="document_vehicle_2",null=True)
    

#testing

