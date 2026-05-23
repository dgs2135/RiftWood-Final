from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('riftwood.urls')),  # Main app URLs
    path('users/', include('users.urls')),  # User-specific URLs
]