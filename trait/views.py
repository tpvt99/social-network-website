from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import View
from .models import Trait
from status.models import Status
from user.models import MyUser

from noti.models import Notification, TraitANotification

# Create your views here.

class AddTraitAjax(View):
    def get(self, request):
        return render(request, 'trait/addtraitajax.html')

class Create(View):
    def post(self, request):
        user_send = request.user
        try:
            user_receive_id = request.POST.get('hiddenfr-t')
            try:
                user_receive_id = int(user_receive_id)
                try:
                    user_receive = MyUser.objects.get(id__exact = user_receive_id)
                except MyUser.DoesNotExist:
                    return HttpResponseRedirect(reverse('web:error'))
            except ValueError:  #ValueError when data is not an integer
                return HttpResponseRedirect(reverse('web:error'))
        except TypeError:  #TypeError when None data
            return HttpResponseRedirect(reverse('web:error'))
        trait_type = request.POST.get('trait_type')
        trait_des = request.POST.get('trait-des')
        if trait_type.strip() and trait_des.strip():
            t = Trait.objects.create(user_send = request.user, user_receive = user_receive, trait_type = trait_type, text = trait_des)
            s = Status.objects.create(user = user_receive, status_type="create-trait", trait = t, privacy="public")
            noti = Notification.objects.create(user = user_receive, noti_type='trait-a')
            TraitANotification.objects.create(noti = noti, trait = t)
        return HttpResponseRedirect(reverse('web:webpage'))
