from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name="index"),
    path('registeras', views.register_page, name="register_page"),
    path('vendor_register', views.registerasvendor, name="registerasvendor"),
    path('customer_register', views.registerascustomer, name="registerascustomer"),
    path('logout/', views.userLogout, name="userLogout"),
    path('login/',views.userLogin,name='userLogin'),
    path('dashboard',views.dashboard,name='dashboard'),
]