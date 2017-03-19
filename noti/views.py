from django.shortcuts import render
from django.views.generic import View
from .models import Notification
import time

# Create your views here.

class NotiAjax(View):
    template = 'noti/notiajax.html'
    def get(self, request):
        user = request.user
        x = request.GET.get('page')
        notis = Notification.objects.filter(user = request.user).order_by('-time')[int(x)*10:int(x)*10+9]
        for i in notis:
            i.read = True
            i.save()
        return render(request, self.template, {'notis':notis})
