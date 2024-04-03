
from django.contrib import admin
from django.urls import path
from store import views


urlpatterns = [
    path('',views.index,name="home"),
    path('collections',views.collections,name="collections"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('add_to_cart/<str:cate_slug>/<str:prod_slug>/', views.add_to_cart, name='add_to_cart'),
    path('buy_now/<str:category_slug>/<str:item_slug>/', views.buy_now, name='buy_now'),
    path('delete_from_cart/<int:pk>/',views.delete_from_cart, name='delete_from_cart'),
]
