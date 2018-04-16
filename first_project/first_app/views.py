from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    webpages_list = models.AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', date_dict)
