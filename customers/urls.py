from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('customers/create/' , views.customer_create_view, name='customer-create'),
    path('customers/list', views.customer_list_view, name="customer-list"),
    path('customers/<str:pk>/update/', views.customer_update_view, name="customer-update"),
    path('customers/delete/', views.customer_delete_view, name="customer-delete"),
    path("customers/detail/<str:pk>/", views.customer_detail_view, name="customer-detail"),
    path("farmer/create/", views.farmer_create_view, name="farmer-create"), 
    path("farmer/list/", views.farmer_list_view, name="farmer-list"), 
    path("farmer/<str:pk>/update/", views.farmer_update_view, name="farmer-update"),
    path("farmer/detail/<str:pk>/", views.farmer_detail_view, name="farmer-detail"),
    path ("farmer/delete", views.farmer_delete_view, name="farmer-delete"),
]
