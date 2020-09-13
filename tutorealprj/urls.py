"""tutorealprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.main, name='main'),
    path('finance/', mainapp.views.finance, name='finance'), #금융 페이지
    path('house/', mainapp.views.house, name='house'), #주거 페이지
    path('welfare/', mainapp.views.welfare, name='welfare'), #복지 페이지
    path('post/', mainapp.views.post, name='post'), #세부 페이지
    path('intro/',mainapp.views.intro, name= 'intro'), #소개 페이지
    path('calendar/', mainapp.views.calendar, name='calendar'), #캘린더 페이지
    path('fi_post_1/', mainapp.views.fi_post_1, name='fi_post_1'), #금융 post 1
    
#==================================================================주거 post
    path('ho_post_1/', mainapp.views.ho_post_1, name='ho_post_1'),
    path('ho_post_2/', mainapp.views.ho_post_2, name='ho_post_2'),
    path('ho_post_3/', mainapp.views.ho_post_3, name='ho_post_3'),
#==================================================================복지 post
    path('wel_post_1/', mainapp.views.wel_post_1, name='wel_post_1'),
    path('wel_post_2/', mainapp.views.wel_post_2, name='wel_post_2'),
    path('wel_post_3/', mainapp.views.wel_post_3, name='wel_post_3'),
]
