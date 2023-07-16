from django.contrib import admin
from apps.houses.models import Properties,Agent

admin.site.register([Properties,Agent])