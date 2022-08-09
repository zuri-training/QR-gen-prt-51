
from django.urls import path
from . import views
from .views import LandingPageView,CONTACTPageView,FAQPageView,ABOUTPageView,DATAPageview,CUSTOMView, DASHBOARDView,TestView
urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('contact/', CONTACTPageView.as_view(), name='contact-us'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('about/', ABOUTPageView.as_view(), name='about'),
    path('datatype/', views.datatype, name='datatype'),
    path('datatype/urltype', views.urltype, name='urltype'),
    path('datatype/texttype', views.texttype, name='texttype'),
    path('datatype/phonetype', views.phonetype, name='phonetype'),
    path('datatype/emailtype', views.emailtype, name='emailtype'),
    path('datatype/preemailtype', views.preemailtype, name='preemailtype'),
    path('datatype/presmstype', views.presmstype, name='presmstype'),
    path('custom/', CUSTOMView.as_view(), name='custom'),
    path('dashboard/', DASHBOARDView.as_view(), name='dashboard'),
     path('test/', TestView.as_view(), name='test_page'),

    
]
