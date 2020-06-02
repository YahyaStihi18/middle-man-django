from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.products,name='products'),
    path('products/<int:product_id>/', views.detail, name='detail'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('gallery/',views.gallery,name='gallery')

]
