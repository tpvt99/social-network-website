from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse, JsonResponse
from .models import Status, StatusVote, StatusComment
from django.db.utils import IntegrityError
from noti.models import Notification, StatusANotification, StatusBNotification, ActANotification, PostANotification
from user.models import MyUser
from act.models import Act, ActFriend
from django.db.models import Q
from friend.models import Friend
from post.models import Post as PostModel
from post.models import PostFriend
import math
from a.settings import BASE_DIR
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

class Content(View):
    template = 'status/status.html'
    def get(self, request):
        idx = request.GET.get('id')
        if idx:
            t = open(BASE_DIR + "/web/static/web/svg.js","r")
            response = HttpResponse(content = t, content_type = 'application/javascript')
            return response
        try:
            page = int(request.GET.get('page'))
        except TypeError:
            return HttpResponse('error')
        fr = Friend.objects.filter(user = request.user).values_list('friend_id', flat=True)
        status = Status.objects.filter(Q(user = request.user) | (Q(user_id__in = list(fr)) & (Q(privacy = 'public') | Q(privacy = 'friend')))).order_by('-time_create')[page*10:page*10 + 10]
        if status:
            return render(request, self.template, {'status':status})
        else:
            return HttpResponse('error')

class Vote(View):
    def get(self, request):
        try:
            t = int(request.GET.get('id'))
        except ValueError:
            return HttpResponse('error')
        status = Status.objects.get(pk__exact = t)
        try:
            vote = StatusVote.objects.create(user = request.user, status = status)
            status.vote += 1
            status.save()
            vote.been_vote = True
            vote.save()
            if request.user != status.user:
                noti = Notification.objects.create(user = status.user, noti_type = 'status-a')
                StatusANotification.objects.create(noti = noti, status = status, who_vote = request.user)
        except IntegrityError:
            vote = StatusVote.objects.get(user = request.user, status = status)
            if vote.been_vote == True:
                status.vote -= 1
                status.save()
                vote.been_vote = False
                vote.save()
            else:
                status.vote += 1
                status.save()
                vote.been_vote = True
                vote.save()
        finally:
            total_friend = len(Friend.objects.filter(user = status.user))
            total_vote = status.vote
            max_percent = math.floor(0.1 * total_friend)
            if max_percent == 0:
                max_percent = 1
            percent = math.floor((total_vote/max_percent) * 100)
            if percent >= 100:
                percent = 100
            response = JsonResponse({'a':vote.been_vote,'vote':percent,'quan':status.vote})
            return  HttpResponse(response)

class SpecificContent(View):
    def get(self, request):
        x = request.GET.get('id')
        status = Status.objects.filter(pk__exact = int(x))
        return render(request, 'status/specific.html',{'status':status})

class Comment(View):
    def post(self, request):
        try:
            status = Status.objects.get(pk__exact = int(request.POST.get('status')))
        except Status.DoesNotExist:
            return HttpResponse('error')
        sc = StatusComment.objects.create(user = request.user, status = status, comment = request.POST.get('comment'))
        if request.user != status.user:
            noti = Notification.objects.create(user = status.user, noti_type = 'status-b')
            StatusBNotification.objects.create(noti = noti, status = status, statuscomment = sc)
        return render(request, 'status/statuscomment.html', {'i':sc})

class Update(View):
    def post(self, request, *a, **kw):
        t = kw.get('type')
        if t == 'privacy':
            try:
                i = Status.objects.get(pk__exact = int(request.POST.get('id')))
            except:
                return HttpResponse('error')
            pri = request.POST.get('privacy')
            i.privacy = pri
            i.save()
            return HttpResponse('ok')

class Create(View):
    def post(self, request):
        data = request.POST
        if (data.get('actin').strip() != '' and data.get('desin').strip() != '') or data.get('actin').strip() != '':
            act = Act.objects.create(user = request.user, head = data.get('actin'), des = data.get('desin'))
            act.province = data.get('province')
            act.province_unicode = data.get('hiddenprovince')
            act.image = request.FILES.get('act-image')
            act.privacy = data.get('privacy')
            act.save()
            # for friend
            fr_id = data.getlist('hiddenfr')
            if fr_id:
                for i in fr_id:
                    t = MyUser.objects.get(pk__exact = int(i))
                    ActFriend.objects.create(act = act, friend = t, accepted = False)
                    noti = Notification.objects.create(user = t, noti_type = 'act-a')
                    ActANotification.objects.create(noti = noti, act = act)
            status = Status.objects.create(status_type = 'act', privacy = act.privacy, act = act, user = request.user)
        elif data.get('desin').strip() != '':
            post = PostModel.objects.create(user = request.user, text = data.get('desin'))
            post.province = data.get('province')
            post.province_unicode = data.get('hiddenprovince')
            post.image = request.FILES.get('act-image')
            post.privacy = data.get('privacy')
            post.save()
            # for friend
            fr_id = data.getlist('hiddenfr')
            if fr_id:
                for i in fr_id:
                    t = MyUser.objects.get(pk__exact = int(i))
                    PostFriend.objects.create(post=post, friend = t)
                    noti = Notification.objects.create(user = t, noti_type = 'post-a')
                    PostANotification.objects.create(noti = noti, post = post)
            status = Status.objects.create(status_type = 'post', privacy =post.privacy, post = post, user = request.user)
        else:
            return HttpResponse('error')
        t = []
        t.append(status)
        return render(request, 'status/status.html',{'status':t})
