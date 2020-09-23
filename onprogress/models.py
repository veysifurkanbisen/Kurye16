from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=50, default="example@email.com")
    getinformation = models.BooleanField(default=False)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + " " + self.surname

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)