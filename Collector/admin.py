from django.contrib import admin
from .models import Connection, PXIConfiguration

# Register your models here.

admin.site.register(Connection)
admin.site.register(PXIConfiguration)