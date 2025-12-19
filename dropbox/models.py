from django.db import models
from django.conf import settings

# Create your models here.

class SecureFile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_files', blank=True)
    content = models.TextField(max_length=300, blank=False)
    is_locked = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner}: {" ".join(self.content.split()[:8])}'
