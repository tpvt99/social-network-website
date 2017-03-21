from django.shortcuts import render
from django.views.generic import View

from .models import Member, GroupInvitation
from .models import Group as GroupModel

from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse

# Create your views here.

class Groups(View):
    def get(self, request):
        return render(request, 'group/groups.html')

class CreateGroup(View):
    def post(self, request):
        name = request.POST.get('group-name')
        privacy = request.POST.get('privacy')
        if name.strip() != '':
            a = GroupModel.objects.create(name = name, privacy = privacy)
            a.admin.add(request.user)
            a.save()
            return HttpResponseRedirect(reverse('group:group', args=(a.id,)))
        else:
            return HttpResponseRedirect(reverse('web:error'))

class Group(View):
    def get(self, request, *a, **kw):
        try:
            idx = kw.get('id')
            try:
                idx = int(idx)
            except ValueError:
                return HttpResponseRedirect(reverse('web:error'))
        except TypeError:
            return HttpResponseRedirect(reverse('web:error'))
        group = GroupModel.objects.get(pk__exact = idx)
        member_id = Member.objects.filter(group = group).values_list('user_id', flat = True)
        group_admin_id = group.admin.all().values_list('id', flat = True)
        if request.user.id in group_admin_id or request.user.id in member_id:
            return render(request, 'group/group.html',{'group':group})
        else:
            return HttpResponseRedirect(reverse('web:error'))
