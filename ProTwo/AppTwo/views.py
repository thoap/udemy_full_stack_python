from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')


def help(request):
    context = {"insert_text": "Help Page"}
    return render(request, "AppTwo/help.html", context)


def user_list(request):

    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print('Error. Invalid Form.')


    return render(request, 'AppTwo/user_list.html', {'form': form})
