from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound

# class-based views

from django.views.generic import View

# models

from activity.models import Activity
from user.models import MyUser, Info
from friend.models import Friend
from plan.models import Plan, PlanParticipants, ParticipantMoreInfo
from scholarship.models import Scholarship
from contest.models import Contest


from django.db.models import Q
import ast
import time
from event.models import Event
from django.utils import timezone

# Create your views here.
class General(View):
    def activity(self):
        return Activity.objects.all()

class Search(View):
    template_activity = 'search/search_activity.html'
    template_event = 'search/search_event.html'
    template_skill = 'search/search_skill.html'
    template_contest = 'search/search_contest.html'
    template_scholarship = 'search/search_scholarship.html'
    template_everyone = 'search/search_everyone.html'
    template_all = 'search/search_all.html'
    template_job = 'search/search_job.html'
    def get(self, request, *a, **kw):
        field = kw.get('field')
        if field == 'activity':
            if request.GET.get('type') != 'all':
                activity = Activity.objects.filter(time_end__gte = timezone.now(), privacy = 'public', activity_type = request.GET.get('type'))
            else:
                activity = Activity.objects.filter(time_end__gte = timezone.now(), privacy = 'public')
            return render(request, self.template_activity,{'activity':activity,'field':'activity'})
        elif field == 'event':
            if request.GET.get('type') != 'all':
                events = Event.objects.filter(time_begin__gte = timezone.now(), privacy = 'public', event_type = request.GET.get('type'))
            else:
                events = Event.objects.filter(time_begin__gte = timezone.now(), privacy = 'public')
            return render(request, self.template_event, {'events':events,'field':'event'})
        elif field == 'everyone':
            return render(request, self.template_everyone,{'val':'0'})
        elif field == 'scholarship':
            scholarships = Scholarship.objects.filter(time_end__gte = timezone.now())
            return render(request, self.template_scholarship, {'scholarships':scholarships})
        elif field == 'contest':
            contests = Contest.objects.filter(privacy = 'public', contest_type = request.GET.get('type'))
            return render(request, self.template_contest, {'contests':contests})
        elif field == 'skill':
            return render(request, self.template_skill)

class InstanceSearch(View):
    template_head = 'search/instancesearch_head.html'
    template_friend = 'search/instancesearch_friend.html'
    template_city = 'search/instancesearch_city.html'
    def get(self, request, *a, **kw):
        if request.is_ajax():
            key = request.GET.get('key')
            field = kw.get('field')
            if field == 'head':
                user = MyUser.objects.filter(fullname__icontains = key)[0:5]
                activity = Activity.objects.filter(head__icontains = key, privacy = 'public',time_begin__gte = timezone.now())[0:3]
                event = []
                if len(user) < 3:
                    event = Event.objects.filter(head__icontains = key, privacy = 'public', time_begin__gte = timezone.now())[0:3]
                return render(request, self.template_head, {'user':user,'activity':activity,'event':event, 'key':key})
            elif field == 'friend':
                user = request.user
                ex = request.GET.get('key1')
                if ex != '[]':
                    ex = ast.literal_eval(ex)
                else:
                    ex = []
                if key:
                    friends = user.friend_friend_user.filter(friend__fullname__icontains = key)
                    for i in ex:
                        friends = friends.exclude(friend__id__exact = i)
                    return render(request, self.template_friend, {'friends':friends})
                else:
                    return HttpResponse('notfound')

class ActivityContent(View):
    template = 'search/activitycontent.html'

    def get(self, request, *a, **kw):
        try:
            page = int(request.GET.get('page'))
            id_post = int(request.GET.get('id'))
            q = request.GET.get('q')
        except TypeError:
            return HttpResponseNotFound('')
        under_limit = 0
        i = 1
        while i < page:
            under_limit += 5
            i+=1

        if q:
            plans = Plan.objects.filter(Q(city__name_ascii__icontains =q) | Q(name__icontains=q) |Q(des__icontains = q)).filter(share__exact = 1)
        else:
            return HttpResponseNotFound('')

        plans = plans[under_limit:under_limit + 5]
        try:
            plan = plans[id_post]
            pp = plan.planparticipants
            try:
                join = False
                info = ParticipantMoreInfo.objects.get(person__id__exact = request.user.id, planparticipants = pp, plan = plan)
                join = info.is_join
                sent = True
            except ParticipantMoreInfo.DoesNotExist:
                sent = False
            return render(request, self.template, {'sent':sent,'join':join,'plan':plan})
        except IndexError:
            return HttpResponseNotFound('')

class Image(View):
    def get(self, request, *a, **kw):
        key = kw.get('field')
        if key:
            key = int(key)
        plan = Plan.objects.get(pk= key)
        image = plan.image.url
        return HttpResponse(image)


class AllContent(View):
    pass

class UserContent(View):
    template = 'search/usercontent.html'
    def get(self, request):
        q = request.GET.get('q')
        user = request.user
        users = MyUser.objects.filter(fullname__icontains = q).exclude(Q(friend_friend_user__friend = user) | Q(id = user.id))
        return render(request, self.template, {'users':users})
