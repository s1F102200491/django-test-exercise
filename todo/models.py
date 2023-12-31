from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)

    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt

class Memo(models.Model):
    task = models.ForeignKey(Task, related_name='memos', on_delete=models.CASCADE)
    memo_text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
