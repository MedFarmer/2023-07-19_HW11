from django.contrib import admin
from django.urls import path, re_path
from app.views import index, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    re_path(r'^profile/(?P<id>\d+)/$', profile, name='profile') # в маршруте показывает id студента
]
