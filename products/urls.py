from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="product-list"),
    path ("product/create/", views.product_create_view, name="product-create"),
    path ("product/<str:pk>/update/", views.product_update_view, name="product-update"),
    path ("product/delete/", views.product_delete_view, name="product-delete"),
    path("buy/create/", views.buy_create_view, name="buy-create"),
    path("buy/list/", views.buy_list_view, name="buy-list"),
    path("buy/<str:pk>/update/",views.buy_update_view ,name="buy-update"),
    path("buy/delete/", views.buy_delete_view, name="buy-delete"),
    path("buy/detail/<str:pk>/", views.buy_detail_view, name="buy-detail"),
    path("sales/create/", views.sale_create_view, name="sale-create"),
    path("sales/list/", views.sale_list_view, name="sale-list"),
    path("sales/<str:pk>/update/", views.sale_update_view, name= "sale-update"),
    path("sales/delete/", views.sale_delete_view, name="sale-delete"),

]
