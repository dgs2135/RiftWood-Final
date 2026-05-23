from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('guitarbuilder/', views.guitarbuilder, name='guitarbuilder'),
    path('bassbuilder/', views.bassbuilder, name='bassbuilder'),
    path('drumsbuilder/', views.drumsbuilder, name='drumsbuilder'),
    path('orders/', views.orders, name='orders'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('guitarbuilder/', views.guitarbuilder, name='guitarbuilder'),
    path('dashboard/order/<int:order_id>/change/', views.admin_change_order_status, name='admin_change_order_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)