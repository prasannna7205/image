from django.db import models

# Create your models here.
class image(models.Model):
    image=models.ImageField(upload_to='my_image')
    date=models.DateTimeField(auto_now_add=True)
