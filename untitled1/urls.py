"""untitled1 URL Configuration
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user1.views import login, vregist, logined, logout, check_code, firstpage, about, gallery, services, contact
from user1.views import add, list1, page, pass1, info,book, cate, column, generate_qrcode


urlpatterns = [
    url(r'^njcx/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^regist/$', vregist, name='vregist'),
    url(r'^logined/$', logined, name='logined'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^check_code/$', check_code),
    url(r'^$', firstpage, name='first'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^service/$', services, name='services'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^add/$', add, name='add'),
    url(r'^list/$', list1, name='list1'),
    url(r'^page/$', page, name='page'),
    url(r'^pass/$', pass1, name='pass1'),
    url(r'^info/$', info, name='info'),
    url(r'^logined/info/$', info, name='info1'),
    url(r'^cate/$', cate, name='cate'),
    url(r'^column/$', column, name='column'),
    url(r'^book/$', book, name='book'),
    url(r'^qrcode/(.+)$', generate_qrcode, name='qrcode'),
    #url(r'^service/$', services, name='services'),
    #url(r'^gallery/$', gallery, name='gallery'),

   # url(r'^about/$',page,name='about',tp='index/about.html'),
    #url(r'^about/$',page,name='about',tp='index/about.html')



]