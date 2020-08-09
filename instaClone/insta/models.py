from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	author= models.ForeignKey('auth.User',on_delete=models.CASCADE)
	image=models.ImageField(blank=True,null=True)
	caption=models.CharField(max_length=255)
	crated_time=models.DateTimeField(default=timezone.now)