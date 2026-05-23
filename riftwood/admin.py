from django.contrib import admin
from .models import CustomOrder, Testimonial, ContactQuery, PageContent

admin.site.register(CustomOrder)
admin.site.register(Testimonial)
admin.site.register(ContactQuery)
admin.site.register(PageContent)