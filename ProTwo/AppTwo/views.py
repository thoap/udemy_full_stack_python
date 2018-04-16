from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return HttpResponse("<em>Hello World!</em>")


def help(request):
    context = {"insert_text": "Help Page"}
    return render(request, "AppTwo/help.html", context)


def user_list(request):
    list_of_users = models.User.objects.order_by('last_name')
    context_dict = {'users': list_of_users}

    return render(request, "AppTwo/user_list.html", context_dict)
