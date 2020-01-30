from django.views.generic import DetailView, ListView
from models import *

class ProjectListView(ListView):
    model = Project

    def get_queryset(self, *args, **kwargs):
        qs = super(ProjectListView, self).get_queryset(*args, **kwargs)
        return qs.filter(active=True)

class ProjectDetailView(DetailView):
    model = Project
