from django.contrib import admin, messages
from django.utils.translation import ngettext

from task.models import Task

    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    actions = ['unassign_selected_tasks']

    @admin.action(description="Enlève l'assignation des tâches sélectionnées")
    def unassign_selected_tasks(self, request, queryset):
        updated = queryset.filter(assignee__isnull=False).update(assignee=None)
        
        if updated == 0:
            self.message_user(
                request,
                "les tâches sélectionnées étaient déjà non assignées",
                messages.ERROR
            )
        else:
            self.message_user(
                request,
                ngettext(
                    "%d tâche a été désassignée avec succès.",
                    "%d tâches ont été désassignées avec succès.",
                    updated
                ) % updated,
                messages.SUCCESS
            )
