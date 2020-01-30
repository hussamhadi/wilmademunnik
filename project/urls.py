from django.conf.urls import url
from project.views import ProjectListView, ProjectDetailView

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='projectlist'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='projectdetail'),
]

