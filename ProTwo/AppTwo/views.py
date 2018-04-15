from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<em>Hello World!</em>")


def help(request):
    context = {"insert_text": "Help Page"}
    return render(request, "AppTwo/help.html", context)
