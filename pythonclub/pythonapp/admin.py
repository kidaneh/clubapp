from django.contrib import admin
from .models import Meeting, Minute, Resource, event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Minute)
admin.site.register(event)
admin.site.register(Resource)
