from django.contrib import admin
from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """ Настроки admin-панели работы с моделей User """

    list_display = ('id', 'email', 'is_active',)
    list_filter = ('id', 'email',)
    ordering = ('is_active',)
