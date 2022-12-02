from django.urls import path
from . import views

urlpatterns = [
    path('', views.visitors ),
    path('<int:id>/', views.visitor_detail),
]