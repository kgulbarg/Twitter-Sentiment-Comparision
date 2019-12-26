from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'index/$', views.index, name='index'),
    #url(r'LSVC/product/$', views.product, name='product'),
    url(r'home/$', views.home, name='home'),
    url(r'products/$', views.products, name='products'),
    url(r'brands/$', views.brands, name='brands'),
    url(r'productanalyze/$', views.productanalyze, name='productanalyze'),
    url(r'brandanalyze/$', views.brandanalyze, name='brandanalyze'),
]