from django.shortcuts import render
from django.views.generic import View
from .models import Image
from django.http import HttpResponseRedirect

# Create your views here.

class Post(View):
    def post(self,request):
        Image.objects.create(image = request.FILES.get('file'), user = request.user, head = request.POST.get('text'), privacy="public")
        return HttpResponseRedirect('/profile/?key=image')
