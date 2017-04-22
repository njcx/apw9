#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from user1.models import User
from django import forms
from django.http import HttpResponse
import qrcode
from cStringIO import StringIO


def index():
    render_to_response("index.html")

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100, widget=forms.TextInput(attrs={'class': 'input input-big',
                                                                                         'placeholder':'登录账号',
                                                                                         'data-validate':'required:请填写账号'}))
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'input input-big',
                                                                                         'placeholder':'登录密码',
                                                                                         'data-validate':'required:请填写密码'}))

def check_code(request):
    import io
    from user1.backend import check_code as CheckCode

    stream = io.BytesIO()
    img, code = CheckCode.create_validate_code()
    img.save(stream, "png")
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())

def loginf(request):
    return render_to_response("login.html")
'''

def login(request):
    if request.method !='POST':
        raise Http404()
    try:
        input_code = request.POST.get('code')
        #input_code.upper(),request.session['CheckCode'].upper())
        user1 =User.objects.get(username = request.POST['name'])
        if user1.password == request.POST['password'] and input_code.upper() == request.session['CheckCode'].upper():
            return HttpResponseRedirect('/logined/')
    except EmptyResultSet:
        pass
'''
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            input_code = request.POST.get('code')
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user and input_code.upper() == request.session['CheckCode'].upper():
                response = HttpResponseRedirect('/logined/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf':uf})

def logined(request):
    return render_to_response('index.html')

def firstpage(request):
    if request.method == 'GET':
        return render_to_response('index/index.html')
    else:
        render_to_response('index/404.html')

def vregist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username= username, password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf})


def index(request):
    username = request.COOKIES.get('username', '')
    return render_to_response('index/index.html', {'username': username})

def logout(request):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response

def about(request):
    if request.method == 'GET':
        return render_to_response('index/about.html')
    else:
        render_to_response('index/404.html')
def services(request):
    if request.method == 'GET':
        return render_to_response('index/services.html')
    else:
        render_to_response('index/404.html')

def gallery(request):
    if request.method == 'GET':
        return render_to_response('index/gallery.html')
    else:
        render_to_response('index/404.html')
def contact(request):
    if request.method == 'GET':
        return render_to_response('index/contact.html')
    else:
        render_to_response('index/404.html')

def add(request):
    if request.method == 'GET':
        return render_to_response('add.html')
    else:
        render_to_response('index/404.html')
def list1(request):
    if request.method == 'GET':
        return render_to_response('list.html')
    else:
        render_to_response('index/404.html')
def page(request):
    if request.method == 'GET':
        return render_to_response('page.html')
    else:
        render_to_response('index/404.html')
def pass1(request):
    if request.method == 'GET':
        return render_to_response('pass.html')
    else:
        render_to_response('index/404.html')

def cate(request):
    if request.method == 'GET':
        return render_to_response('cate.html')
    else:
        render_to_response('index/404.html')
def info(request):
    if request.method == 'GET':
        return render_to_response('info.html')
    else:
        render_to_response('index/404.html')
def book(request):
    if request.method == 'GET':
        return render_to_response('book.html')
    else:
        render_to_response('index/404.html')
def column(request):
    if request.method == 'GET':
        return render_to_response('column.html')
    else:
        render_to_response('index/404.html')
def generate_qrcode(request, data):
    img = qrcode.make(data)
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2017 04:11:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response