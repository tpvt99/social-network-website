# response

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse

# class-based view

from django.views.generic import View

# settings

from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# models

from user.models import MyUser, Info
import re
# Create your views here.


class FrontPage(View):
    template = 'frontpage/frontpage.html'
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('web:webpage'))
        return render(request, self.template)

class LogForm(View):
    template = 'frontpage/logform.html'
    def get(self, request):
        return render(request, self.template)

class RegForm(View):
    template = 'frontpage/regform.html'
    def get(self, request):
        return render(request, self.template)
class Helper(View):
    def validateEmail(self, email):
        t = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if t.match(email) and t.match(email).group() == email:
            return True
        return False

    def validateName(self, name):
        z = name.split(' ')
        for i in z:
            if not i.isalpha():
                return False
        return True

class Register(Helper):
    def post(self, request):
        firstname = request.POST.get('regfirst')
        lastname = request.POST.get('reglast')
        fullname = firstname + ' ' + lastname
        password = request.POST.get('regpass')
        repassword = request.POST.get('regrepass')
        email = request.POST.get('rege')
        sex = request.POST.get('sex')
        try:
            firstname = firstname.strip()
            lastname = lastname.strip()
            password = password.strip()
            repassword = repassword.strip()
            email = email.strip()
        except:
            return render(request, 'frontpage/frontpage.html',{'email':email,'firstname':firstname,'lastname':lastname,'total_error':'Có lỗi xảy ra. Vui lòng thử lại'})
        if len(password) < 6:
            return render(request, 'frontpage/frontpage.html',{'email':email,'firstname':firstname,'lastname':lastname,'password_error':'Mật khẩu nhỏ hơn 6 kí tự'})
        if password != repassword:
            return render(request, 'frontpage/frontpage.html',{'email':email,'firstname':firstname,'lastname':lastname,'password_error':'Mật khẩu không trùng khớp'})
        if not self.validateEmail(email):
            return render(request, 'frontpage/frontpage.html',{'email':email,'firstname':firstname,'lastname':lastname,'email_error':'Email đăng kí không hợp lệ'})
        if not self.validateName(firstname) or not self.validateName(lastname):
            return render(request, 'frontpage/frontpage.html',{'email':email,'firstname':firstname,'lastname':lastname,'name_error':'Tên không hợp lệ'})
        try:
            MyUser.objects.get(email = email.strip())
            return render(request, 'frontpage/frontpage.html',{'email':email,'email_error':'Email này đã được đăng ký'})
        except MyUser.DoesNotExist:
            user = MyUser.objects.create_user(
                            email = email,
                            fullname = fullname,
                            password = password)
            info = Info.objects.create(user = user, firstname = firstname, lastname = lastname, sex = sex)
            login(request, user)
            return HttpResponseRedirect(reverse('web:webpage'))
        
class Login(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email = email, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('web:webpage'))
        return render(request, 'frontpage/login_error.html', {'error':'Email sai hoặc mật khẩu không chính xác','email':email})

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('frontpage:frontpage'))
