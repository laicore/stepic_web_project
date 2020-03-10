"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from .wsgi import fun
from qa.views import *

urlpatterns = [
    path('', include('qa.urls1')),
    path('admin/', admin.site.urls),
    path('login/', fun),
    path('signup/', fun),
    re_path(r'question/(?P<id>\d+)/', getQ),
    path('ask/', include('qa.urls')),
    path('popular/', include('qa.urls1')),
    path('new/', fun)

]
