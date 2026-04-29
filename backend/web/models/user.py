import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now,localtime


def photo_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'#uuid.dd==uuid4取随机字符串，.hex取16进制，:10取前10位
    return f'user/photos/{instance.user_id}_{filename}'#instance为数据库对象


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo =models.ImageField(default='user/photos/default.png', upload_to=photo_upload_to)
    profile = models.TextField(default='该用户还没有填写简介',max_length=500)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.user.username} - {localtime(self.create_time).strftime('%Y-%m-%d %H:%M:%S')}'
