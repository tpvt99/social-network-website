from django.shortcuts import render
from django.views.generic import View
from .models import MessageUser, Message
from user.models import MyUser
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

class Ajax(View):
    template = 'message/ajax.html'
    def get(self, request):
        return render(request, self.template)

class MessageView(View):
    template = 'message/message.html'
    def get(self, request):
        return render(request, self.template)

class CreateMessAjax(View):
    template = 'message/createmessajax.html'
    def get(self, request):
        return render(request, self.template)
    def post(self, request):
        u_id = request.POST.get('input-fr');
        try:
            u_id = int(u_id)
        except:
            return HttpResponseRedirect(reverse('message:message'))
        user = MyUser.objects.get(pk__exact = u_id)
        chat_buddies = request.user.message_messageuser_user.all()
        #this is writing for 2 person chatting
        has_buddy = False
        for i in chat_buddies:
            if user in i.user.all() and request.user in i.user.all() and len(i.user.all()) == 2:
                has_buddy = True
                i.last_active = timezone.now()
                i.read = False
                i.save()
                Message.objects.create(user_send = request.user, chat_buddies = i, text = request.POST.get('input-mess'))
                break
        if has_buddy == False:
            m = MessageUser.objects.create(last_active = timezone.now())
            m.user.add(request.user)
            m.user.add(user)
            m.save()
            Message.objects.create(user_send = request.user, chat_buddies = m, text = request.POST.get('input-mess'))
        return HttpResponseRedirect(reverse('message:message'))

