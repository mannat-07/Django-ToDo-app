from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)  # The task text
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when created
    completed = models.BooleanField(default=False)  # For checkbox feature

    def __str__(self):
        return self.name  # Shows task name in admin/debug