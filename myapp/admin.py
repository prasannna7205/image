from django.contrib import admin
from .models import image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image','date']
admin.site.register(image, ImageAdmin)
