"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
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

from app import views

urlpatterns = [
    # 127.0.0.1:8080/admin/
    url(r'^admin/', admin.site.urls),
    # 127.0.0.1:8080/hello/
    url(r'^hello/', views.hello),
    # 127.0.0.1:8080/create_stu/
    url(r'^create_stu/', views.create_stu),
    url(r'^sel_stu/', views.sel_stu),
]
