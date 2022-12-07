from django.urls import path
from . import views

app_name = 'visitors'

urlpatterns = [
    path('', views.visitors, name="list" ),
    path('register/$', views.visitor_register, name="register"),
    path('<int:id>/', views.visitor_detail, name="detail"),
    
]