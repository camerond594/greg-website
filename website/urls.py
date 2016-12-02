from django.conf.urls import url
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from greg import settings
from . import views

urlpatterns = [
    url(r'^$', views.base_site, name='base_site'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^about/$', views.about, name='about'),
    url(r'^criminal_law/$', views.criminal, name='criminal'),
    url(r'^civil_litigation/$', views.civil, name='civil'),
    url(r'^drug_law/$', views.drug, name='drug'),
    url(r'^family_law/$', views.family, name='family'),
    url(r'^contact/$', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()