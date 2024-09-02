from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="ShopHome") ,
    path('about', views.about, name="AboutUs") ,
    path('contact/', views.contact, name="contactUs") ,
    path('tracker', views.tracker, name="TrackingStatus") ,
    path('search', views.index, name="Search") ,
    path('products/<int:myid>', views.productview, name="ProductView") ,
    path('checkout', views.checkout, name="CheckOut") ,
    path('finalpage', views.checkout, name="finalpage") ,
]
