from django.urls import path , reverse
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('online_store', views.online_store, name='online_store'),
    path('product/', views.product, name='product'),
    path('category/', views.category, name='category'),
    path('cart/', views.view_cart, name='view_cart'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path("signupsuccessful/" , views.signupsuccessful , name = "signupsuccessful"),
    path("order/" , views.order , name = "order"),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product_details/<int:id>', views.product_details, name = "product_details"),
    path('category_details/<int:id>', views.category_details, name = "category_details"),
    path('add_to_cart/<int:id>',views.add_to_cart , name='add_to_cart' ),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)