"""pr2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#zapis przeniesiony do urls.py w kat. shelfs
# from shelf.views import AuthorListView, AuthorDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^authors/$', AuthorListView.as_view()),

# Ponizsze wpisy zostaly przenisione do pliku urls.py w kat. shelfs.  
#    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
#    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),

# Jezeli w adresie zostanie wykryty ciag "authors" dalsza analiza pliku przejdzie to urls.py w kat. shelfs
#    url(r'^authors/', include('shelf.urls') ), 

# Mala zmiana, authors zostaly przeniesione do urls.py shelf, a na ich miejsce wstawiony shelf poniewaz oprocz authors beda books i wydawcy
    url(r'^shelf/', include('shelf.urls', namespace='shelf') ), 

]
