
from django.contrib import admin
from django.urls import path
from .views import index, details, checkout, confirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:myid>', details, name='details'),
    path('checkout/', checkout, name='checkout'),
    path('confirmation/', confirmation, name='confirmation'),
]
