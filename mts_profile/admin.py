from django.contrib import admin
from .models import Booking, Testimonial , Team , TeamOnSite
from online_store.models import Product, Category, Cart , Profile , Order 

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service', 'viewed')
    list_filter = ('viewed','service',)
    empty_value_display = 'N/A'
admin.site.register(Booking, BookingAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Testimonial, TestimonialAdmin)

class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Team, TeamAdmin)

admin.site.register(TeamOnSite)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product','order_date','viewed',  'received' , )
    list_filter = ('viewed','received')
    empty_value_display = 'N/A'
admin.site.register(Order, OrderAdmin)

# class ReceivedItemAdmin(admin.ModelAdmin):
#     list_display = ('user','product','received_date')
#     list_filter = ('received_date',)
#     empty_value_display = 'N/A'
# admin.site.register(ReceivedItem,ReceivedItemAdmin)

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'price', 'category' , 'quantity')
    list_filter = ('category',)
    empty_value_display = 'N/A'
admin.site.register(Product, ProductAdmin)

# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product',  )
#     list_filter = ('product',)
#     empty_value_display = 'N/A'
# admin.site.register(Cart, CartAdmin)




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', )
    list_filter = ('address',)
    empty_value_display = 'N/A'
admin.site.register(Profile, ProfileAdmin)


