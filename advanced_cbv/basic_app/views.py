from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView,
    DeleteView
)
from django.core.urlresolvers import reverse_lazy
from . import models


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    # def get_context_data(self):
    #     context =


class SchoolListView(ListView):
    """docstring for SchooListView"""
    context_object_name = "schools"
    model = models.School


class SchoolDetailView(DetailView):
    """docstring for SchoolDetailView"""
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
