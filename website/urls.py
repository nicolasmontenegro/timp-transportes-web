from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^nosotros', views.aboutUs, name='Nosotros'),	
	url(r'^servicios', views.services, name='Servicios'),
]