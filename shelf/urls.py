from django.conf.urls import include, url 
from django.contrib import admin
from shelf.views import AuthorListView, AuthorDetailView

urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),

        ]


