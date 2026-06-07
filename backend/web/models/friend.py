from time import localtime

from django.db import models
from django.utils import timezone
from web.models.character import Character
from web.models.user import UserProfile


class Friend(models.Model):
    me  = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    memory = models.TextField(default="",max_length=5000)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.character.name} - {self.me.user.username} - {timezone.localtime(self.create_time).strftime('%Y-%m-%d %H:%M:%S')}"


