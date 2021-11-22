from django.urls import path,include,re_path
from . import views

urlpatterns =[
        path('',views.index,name='index'),
        path('api/get',views.search),
        path('api/post',views.add_products),
        path('product/<int:product_id>',views.product_by_id, name='product_by_id'),
        ]

