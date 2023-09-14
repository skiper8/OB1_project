from django.contrib import admin

from users.models import User


@admin.register(User)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'token', 'token')
    search_fields = ('email',)
    list_filter = ('token',)

