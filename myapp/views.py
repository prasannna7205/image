from django.shortcuts import render
from .forms import ImageView
from .models import image

# Create your views here.
def home(request):
    if request.method =='POST':
        form=ImageView(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageView()
    img=image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})
