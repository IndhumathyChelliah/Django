from django.contrib import admin
from django.urls import path,include
from karthiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('info/',views.info,name='info'),
    path('success/',views.success,name='success')
]