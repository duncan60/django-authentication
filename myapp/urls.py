"""myapp URL Configuration

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
from django.urls import path, include
from .router import router


urlpatterns = [
    path('versionInfo/', include('versionInfo.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

admin.site.site_header = "管理系統"
admin.site.site_title = "管理系統 Portal"
admin.site.index_title = "歡迎來到 管理系統 Portal"
