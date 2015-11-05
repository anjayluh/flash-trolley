from django.conf.urls import patterns, include, url
from flashTrolley.views import  Register,Login,logout_page, view_product, AddProduct,admin_product, view_customer,delete_product
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^register/$',Register.as_view()),
                       url(r'^$', view_product, name='home'),
                       url(r'^home/$', view_product),
                       url(r'^signin/$', Login.as_view()),
                       url(r'^logout/$',logout_page),
                       url(r'^flashtrolley/$', TemplateView.as_view(template_name = 'flashTrolleyAdmin/index.html')),
                       url(r'^viewproducts/$',admin_product),
                       url(r'^deleteproduct/$',delete_product),
                       url(r'^viewcustomers/$',view_customer),
                       url(r'^addproduct/$',AddProduct.as_view()),
                       url(r'^contact/$',TemplateView.as_view(template_name= 'flashTrolley/contact.html')),
                       url(r'^about/$',TemplateView.as_view(template_name= 'flashTrolley/about.html')),
                       url(r'^wishlist/$',TemplateView.as_view(template_name='flashTrolley/wishlist.html')),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
                       )
