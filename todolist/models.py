from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True ) # on_delete = jika User hilang, semua task juga hilang; #null=True => database boleh empty field
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    isFinished = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title


   