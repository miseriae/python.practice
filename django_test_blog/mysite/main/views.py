from django.shortcuts import render
from .models import BlogPost
#from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"posts": BlogPost.objects.all})
                  