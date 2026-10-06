from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
   path('admin/', admin.site.urls),
   path("", views.homepage, name='homepage'),
   path("apps/", include('apps.urls')),
]