# Register your models here.
from django.contrib import admin

from users.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')