from django.urls import path
from . import views


urlpatterns = [
    path("account/register/", views.register_view, name="register"),
    path('account/login/' , views.login_view, name='login'),
    path('account/logout', views.logout_view , name='logout')
]