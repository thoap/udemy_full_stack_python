from django.conf.urls import url
from . import views

# Template tagging (global name for this app)
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.rel_urls, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
