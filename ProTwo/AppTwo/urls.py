from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^help/$', views.help, name='help'),
]
