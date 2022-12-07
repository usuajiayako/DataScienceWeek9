
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('visitors/', include('visitors.urls')),
    path('about/', views.about),
    path('', accounts_views.login_view, name = 'home')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)