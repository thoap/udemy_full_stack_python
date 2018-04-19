from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def other(request):
    return render(request, 'basic_app/other.html')


def rel_urls(request):
    return render(request, 'basic_app/relative_url_templates.html')
