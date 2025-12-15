from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('destinations.urls')),
    path('api/', include('plans.urls')),
    path('api/', include('accounts.urls')),
]
