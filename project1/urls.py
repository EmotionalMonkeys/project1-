from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.homepage, name='homepage'),
	url(r'^signup/$', views.signup, name='signup'),

	url(r'^login/$', views.login, name='login'),
	url(r'^auth/$', views.auth_view, name='auth'),

	url(r'^product/$', views.product, name='product'),
	url(r'^product/(?P<pk>\d+)/$', views.product, name='product'),

	url(r'^product/search/$', views.product_search, name='product_search'),

	url(r'^product/new/$', views.product_new, name='product_new'),
	url(r'^product/edit/(?P<pk>\d+)/$', views.product_edit, name='product_edit'),
	url(r'^product/delete/(?P<pk>\d+)/$', views.product_delete, name='product_delete'),
	url(r'^category/$', views.category, name='category'),
	url(r'^category/new/$', views.category_new, name='category_new'),

  url(r'^category/edit/(?P<pk>\d+)/$', views.category_edit, name='category_edit'),
  url(r'^category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete'),

  url(r'^product_browse/$', views.product_browse, name='product_browse'),
  url(r'^product_browse/(?P<pk>\d+)/$', views.product_browse, name='product_browse'),

  url(r'^product_order/(?P<pk>\d+)/$', views.product_order, name='product_order'),

  url(r'^shopping_cart/$', views.shopping_cart, name='shopping_cart')

  #url(r'^signup/sucess/$', views.signupSucess, name='signupSucess'),
]

 

