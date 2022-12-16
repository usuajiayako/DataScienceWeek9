from django.urls import path
from . import views

app_name = 'visitors'

urlpatterns = [
    path('', views.visitors, name="list" ),
    path('register/', views.visitor_register, name="register"),
    path('<int:id>/', views.visitor_detail, name="detail"),
    path('report/', views.visitor_report, name="report"),
    path('dashboard/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('dashboard/data/', views.pivot_data, name='pivot_data'),
]