from django.db import models

from developer.models import Developer

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(
        Developer, 
        related_name="tasks",
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        verbose_name="assignee"
    )

    class Meta:
       permissions = [
           ('task_management', 'Can create, assign and delete tasks'),
       ]
    
    def __str__(self):
        return f"{self.title} {self.description}"