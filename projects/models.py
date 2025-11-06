from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    priority = models.IntegerField(unique=True)
    deadline = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='tasks_images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks_demo')

    def __str__(self):
        return f"{self.title} (Prioridad {self.priority})"

def post_upload_to(instance, filename):
        return f"projects/{filename}"
