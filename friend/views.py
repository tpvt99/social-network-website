# response

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.db.models import Q
# class-based view

from django.views.generic import View

# models

from .models import AddFriend as AddFriendModel
from user.models import MyUser
from .models import Friend
import random

# error 
from django.db.utils import IntegrityError

# Create your views here.

class AddFriend(View):
    def post(self, request):
        if request.user.is_authenticated() and request.is_ajax():
            inviter = request.user
            try:
                receiver = MyUser.objects.get(pk__exact = int(request.POST.get('key')))
            except MyUser.DoesNotExist:
                return HttpResponse('error')
            if request.POST.get('action') == 'connect':
                try:
                    friend = Friend.objects.get(user = inviter, friend = receiver)
                    return HttpResponse('error')
                except Friend.DoesNotExist:
                    try:
                        t = AddFriendModel.objects.get(inviter = receiver, receiver = inviter, is_friend = False)
                        return HttpResponse('error')
                    except AddFriendModel.DoesNotExist:
                        try:
                            t = AddFriendModel.objects.create(inviter = inviter, receiver = receiver, is_friend = False)
                            return HttpResponse('ok')
                        except IntegrityError:
                            return HttpResponse('error')
            elif request.POST.get('action') == 'accept':
                try:
                    friend = Friend.objects.get(user = inviter , friend = receiver)
                    return HttpResponse('error')
                except Friend.DoesNotExist:
                    try:
                        t = AddFriendModel.objects.get(inviter = inviter, receiver = receiver, is_friend = False)
                        return HttpResponse('error')
                    except AddFriendModel.DoesNotExist:
                        try:
                            t = AddFriendModel.objects.get(inviter = receiver, receiver = inviter, is_friend = False)
                            t.is_friend = True
                            t.save()
                            Friend.objects.create(user = inviter, friend = receiver)
                            Friend.objects.create(user = receiver, friend = inviter)
                            return HttpResponse('ok')
                        except AddFriendModel.DoesNotExist:
                            return HttpResponse('error')
            elif request.POST.get('action') == 'decline':
                try:
                    Friend.objects.get(user = inviter, friend = receiver)
                    return HttpResponse('error')
                except Friend.DoesNotExist:
                    try:
                        t = AddFriendModel.objects.get(inviter = inviter, receiver = receiver, is_friend = False)
                        t.delete()
                        return HttpResponse('ok')
                    except AddFriendModel.DoesNotExist:
                        return HttpResponse('error')
            elif request.POST.get('action') == 'refuse':
                try:
                    Friend.objects.get(user = inviter, friend = receiver)
                    return HttpResponse('error')
                except Friend.DoesNotExist:
                    try:
                        t = AddFriendModel.objects.get(inviter = receiver, receiver = inviter, is_friend = False)
                        t.delete()
                        return HttpResponse('ok')
                    except AddFriendModel.DoesNotExist:
                        return HttpResponse('error')
        else:
            return HttpResponseRedirect(reverse('frontpage:frontpage'))

class FriendRequest(View):
    template = 'friend/request.html'
    def get(self, request):
        if request.user.is_authenticated():
            user = MyUser.objects.get(pk__exact = request.user.id)
            requests = user.friend_addfriend_receiver.filter(is_friend = False)
            for i in requests:
                i.read = True
                i.save()
            return render(request, self.template, {'requests':requests})

class Search(View):
    template = 'search/search_everyone.html'
    def get(self, request):
        name = request.GET.get('name')
        page = request.GET.get('page')
        fr_list = Friend.objects.filter(user = request.user).values_list('friend_id', flat=True)
        if name and name.strip() != '':
            #user = MyUser.objects.filter(fullname__icontains = name).exclude(pk__exact = request.user.id).exclude(pk__in = list(fr_list))[10*int(page):10*int(page)+9]
            user = MyUser.objects.filter(fullname__icontains = name).exclude(pk__exact = request.user.id)[10*int(page):10*int(page)+9]
            return render(request, self.template, {'users':user,'val':0})
        return render(request, self.template, {'val':0})

class FriendAjax(View):
    template = 'friend/friendajax.html'
    def get(self, request):
        friend_request = AddFriendModel.objects.filter(receiver = request.user, is_friend = False)
        for i in friend_request:
            i.read = True
            i.save()
        friend_id = Friend.objects.filter(user = request.user).values_list('friend_id', flat = True)
        user = MyUser.objects.exclude(id__in = friend_id)
        if len(user)>5:
            t = random.sample(range(len(user)),5)
            friend_suggest = []
            for i in t:
                friend_suggest.append(user[i])
        else:
            friend_suggest = []
        return render(request, self.template, {'friend_request':friend_request,'friend_suggest':friend_suggest})
