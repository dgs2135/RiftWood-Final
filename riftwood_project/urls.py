from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('riftwood.urls')),  # Main app URLs
    path('users/', include('users.urls')),  # User-specific URLs
]
