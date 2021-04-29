from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )

@admin.register(PhoneCode)
class PhoneCodeAdmin(admin.ModelAdmin):
    list_display = (
        'code',
    )

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(AddressUser)
class AddressUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

