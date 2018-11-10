"""Learn_Template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url,include
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_time/',views.show_time),
    path('query/',views.query),
    path('login/',views.login,name="login"),
    url(r'^backend/$',views.backend),
    url(r'^backend/student/',views.student,name='student'),
    
    # 单表操作
    url(r'^indexDB/$',views.indexDB),
    url(r'^indexDB/addBook',views.addBook,name='addbook'),
    url(r'^indexDB/updateBook',views.updateBook,name='updatebook'),
    url(r'^indexDB/deleteBook',views.deleteBook,name='deletebook'),
    
    # 查询
    url(r'^indexDB/queryBook',views.queryBook,name='querybook'),
]
