from django.shortcuts import render

# Create your views here.
from dajngo.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.core.urlresolvers import reverse
from django.views import generic

from . import models


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = models.Group


class SingleGroup(generic.DetailView):
    """docstring for SingleGroup"""

    model = models.Group


class ListGroups(generic.ListView):
    """docstring for ListGroups"""

    model = models.Group
