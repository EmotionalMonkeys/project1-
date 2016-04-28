from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^product', views.product, name='product'),
    url(r'^category', views.category, name='category'),
    url(r'^category/new/$', views.category_new, name='category_new'),



]
