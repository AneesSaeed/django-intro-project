from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from developer.forms import DeveloperForm, DeveloperChangeForm
from developer.models import Developer
from task.models import Task

class TaskInLine(admin.StackedInline):
    model = Task
    extra = 1


@admin.register(Developer)
class DeveloperAdmin(UserAdmin):
    add_form = DeveloperForm
    form = DeveloperChangeForm
    model = get_user_model()
    list_display = ('first_name', 'last_name', 'username', 'is_free')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2'),
        }),
    )

    inlines = [TaskInLine]