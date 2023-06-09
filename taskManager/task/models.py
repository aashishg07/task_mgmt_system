from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user"),

    def __str__(self):
        return self.title
    
