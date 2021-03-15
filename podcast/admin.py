from django.contrib import admin
from .models import Episode, Host


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'host')
    list_filter = ('created',)


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
