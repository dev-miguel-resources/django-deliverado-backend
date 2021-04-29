from django.contrib import admin
from .models import *


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )



@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',

        
    )


@admin.register(TypeProduct)
class TypeProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
    )


@admin.register(ExperienceProduct)
class ExperienceProductAdmin(admin.ModelAdmin):
    list_display = (
        'experience',
        'product'
    )


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'product',
    )


@admin.register(FeaturedShop)
class FeaturedShopAdmin(admin.ModelAdmin):
    list_display = (
        'shop',
    )


@admin.register(PromotionShop)
class PromotionShopAdmin(admin.ModelAdmin):
    list_display = (
        'shop',
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(OrderHistoryStatus)
class OrderHistoryStatusAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'order',
    )


@admin.register(MessageOrder)
class MessageOrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )
@admin.register(FeedbackOrder)
class FeedbackOrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(ReportOrder)
class ReportOrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(DataGPS)
class AddressUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )


@admin.register(CategoryGroup)
class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
 
@admin.register(ExperienceGroup)
class ExperienceGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(UserShop)
class UserShopAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'shop',
    )