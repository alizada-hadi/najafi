from django.urls import path
from . import views
urlpatterns = [
    path('employee/list', views.employee_list_view, name='employee-list'), 
    path("employee/create/", views.employee_create_view, name="employee-create"),
    path("employee/<str:pk>/update/", views.employee_update_view, name="employee-update"),
    path("employee/delete/", views.employee_delete_view, name="employee-delete")

]
