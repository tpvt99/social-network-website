from django.shortcuts import render
from django.views.generic import View
from .models import MessageUser, Message
from user.models import MyUser
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
import time

from django.core.urlresolvers import reverse

# Create your views here.

class Ajax(View):
    template = 'message/ajax.html'
    def get(self, request):
        return render(request, self.template)

class MessageView(View):
    template = 'message/message.html'
    def get(self, request):
        return render(request, self.template)

class HandleMessageBuddy(View):
    def buddy(self, user1, user2): # for 2 people only user1 is requestuser
        chat_buddies = user1.message_messageuser_user.all()
        for i in chat_buddies:
            if user1 in i.user.all() and user2 in i.user.all() and len(i.user.all()) == 2:
                return i
        m = MessageUser.objects.create(last_active = timezone.now())
        m.user.add(user1)
        m.user.add(user2)
        m.save()
        return m
    
    # [{'a':'a'},{'a':'c},{'b':aa'}] to [{'a':['a,'c']},{'b':['aa']}]
    def mess_collect(self, mess):
        x= []
        for i in mess:
            x.append({i.user_send:i})
        print(x)
        t=[]
        final = []
        last_val = 0
        for i in x:
            for z in i.keys():
                if len(t) == 0:
                    t.append(z)
                else:
                    if z != t[-1]:
                        t.append(z)
        print(t)
        for i in range(0,len(t)):
            aa = {}
            aa[t[i]] = []
            br = False
            for m in range(last_val,len(x)):
                for key,value in x[m].items():
                    if key != t[i]:
                        br = True
                        break
                    aa[key].append(value)
                    last_val += 1
                if br == True:
                    break
            final.append(aa)
            return final


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

class ChatBoxAjax(HandleMessageBuddy):
    def get(self, request): #user1 is request, user2 is receive_user
        user1 = request.user
        try:
            user2_id = request.GET.get('id')
            try:
                user2_id = int(user2_id)
                user2 = MyUser.objects.get(id = user2_id)
            except ValueError:
                return HttpResponseRedirect(reverse('web:error'))
        except TypeError:
            return HttpResponseRedirect(reverse('web:error'))
        messageuser = self.buddy(user1, user2)
        return render(request, 'message/mess-ajax-web.html', {'user2':user2, 'messageuser':messageuser})

class AjaxGetMess(HandleMessageBuddy):
    def get(self, request):
        typex = request.GET.get('type')
        if typex == 'first-time':
            try:
                user2_id = int(request.GET.get('user2_id'))
                user2 = MyUser.objects.get(pk__exact = user2_id)
            except:
                return HttpResponse('error')
            messagebuddy = self.buddy(request.user, user2)
            mess = Message.objects.filter(chat_buddies = messagebuddy)
            for i in mess:
                i.read = True
                i.save()
            return render(request, 'message/mess-conversation-boddy.html', {'mess':mess,'user1':request.user.id,'user2':user2_id})
        elif typex == 'second':
            try:
                user2_id = int(request.GET.get('user2_id'))
                user2 = MyUser.objects.get(pk__exact = user2_id)
            except:
                return HttpResponse('error')
            messagebuddy = self.buddy(request.user, user2)
#            time_out = 3
#            time_start = time.time()
#            while time.time() < time_start + time_out:
            mess = Message.objects.filter(chat_buddies = messagebuddy, read = False).exclude(user_send = request.user)
            if mess:
                for i in mess:
                    i.read = True
                    i.save()
                return render(request, 'message/mess-conversation-boddy.html', {'mess':mess,'user1':request.user.id,'user2':user2_id})
            return HttpResponse('error')

class AjaxSendMess(View):
    def post(self, request):
        try:
            mess = request.POST.get('mess')
            mess = mess.strip()
        except:
            return HttpResponse('error')
        try:
            messbuddyid = int(request.POST.get('mu'))
            messbuddy = MessageUser.objects.get(pk__exact = messbuddyid)
        except:
            return HttpResponse('error')
        m = Message.objects.create(user_send = request.user, chat_buddies = messbuddy, text = mess)
        return render(request, 'message/mess-conversation-boddy.html', {'mess':[m], 'user1':request.user.id, 'user2':18})
