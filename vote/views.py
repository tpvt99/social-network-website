from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import View
from django.db.utils import IntegrityError

# Create your views here.

class ActivityView(View):
    def get(self, request, *a, **kw):
        pass
