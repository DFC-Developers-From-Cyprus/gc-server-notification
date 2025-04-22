import uuid
from django.db import models

class Notification(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user_uuid = models.UUIDField()
    message = models.TextField()
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}: {self.message[:30]}"