from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'^category/new/$',views.category_new, name='category_new'),
    url(r'^category/edit/(?P<pk>\d+)/$', views.category_edit, name='category_edit'),
    
    ]
