from django.urls import path
from . import views

app_name = 'visitors'

urlpatterns = [
    path('', views.visitors, name="list" ),
    path('<int:id>/', views.visitor_detail, name="detail"),
]