"""django_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from backend import views  # 导入views.py文件中的index函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('index', views.index),  # 在url中凡是以url开头的访问都使用index函数来处理该请求
    # 将主页指向vue工程
    url(r'^balanced_binary_tree', views.balanced_binary_tree),
    url(r'^huffman_encode', views.huffman_encode),
    url(r'^huffman_decode', views.huffman_decode),
    url(r'^cipher', views.cipher),
    url(r'^message_save', views.message_save),
    url(r'^message_load', views.message_load),
    url(r'^show_tree', views.family_tree_creat),
]
