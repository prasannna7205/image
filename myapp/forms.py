from django import forms
from .models import image

class ImageView(forms.ModelForm):
    class Meta:
        model=image
        fields='__all__'
        labels={'image':''}