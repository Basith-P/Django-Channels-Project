from django.contrib import admin

from .models import DataItem, Statistic

admin.site.register(Statistic)
admin.site.register(DataItem)
