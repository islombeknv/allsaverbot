from django.contrib import admin

from .models import TelegramUserModel


@admin.register(TelegramUserModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'lang']
    list_display = ['tg_id', 'username', 'first_name', 'lang']
    search_fields = ['tg_id', 'username', 'first_name', 'last_name']