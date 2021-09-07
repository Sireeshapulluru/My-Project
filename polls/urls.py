from django.urls import path

from . import views

urlpatterns = [

	path('', views.index, name="index"),
	path('home/', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('choice/' ,views.choice, name="chioce"),
	path('register/', views.register, name="register"),

]
