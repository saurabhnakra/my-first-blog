from django.conf.urls import url

from . import views
app_name = 'website'
urlpatterns = [
	url(r'^$', views.IndexView, name='index'),
	url(r'^index.html/$', views.IndexView, name='index2'),
	url(r'^about.html/$', views.AboutView, name='about'),
	url(r'^contact.html$', views.ContactView, name='contact'),
]