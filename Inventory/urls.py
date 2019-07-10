
from django.urls import path
from . import views
urlpatterns = [
    path('insert/',views.insert, name='insert'),
    path('CustomerOrder/',views.customer, name='CustomerOrder'),
    path('InventoryStatus/', views.storage, name='InventoryStatus'),
    path('Home/',views.index, name='Home'),
    path('',views.index, name='index'),
    path('submit/',views.submit, name='submit'),
    ]
