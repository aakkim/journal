from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_journal', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def created_date(self):
        return self.created_at.strftime('%B %d %Y')