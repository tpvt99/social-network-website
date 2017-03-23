from django.db import models
from django.conf import settings

# Create your models here.

def image_upload(instance, filename):
    return 'image/user_{0}/{1}'.format(instance.user.id, filename)

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    time_create = models.DateTimeField(auto_now_add = True)
    head = models.CharField(max_length = 200, null = True) #2
    privacy = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = image_upload)
