"""py3_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from blog import views as blog_views
from mysql import views as mysql_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index),
    path('blog/', blog_views.blog_index),
    path('home/', blog_views.blog_home),
    path('add/', blog_views.add2, name='add2'),
    path('add/<int:a>/<int:b>/', blog_views.add2, name='add2'),
    path('add_home/', blog_views.add_index),

    path('order', mysql_views.mysql_index),
    path('report', mysql_views.report),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
