
from django.urls import path
from .views import LandingPageView,CONTACTPageView,FAQPageView,ABOUTPageView,DATAPageview,CUSTOMView, DASHBOARDView,TestView
urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('contact/', CONTACTPageView.as_view(), name='contact-us'),
    path('faq/', FAQPageView.as_view(), name='faq'),
    path('about/', ABOUTPageView.as_view(), name='about'),
    path('datatype/', DATAPageview.as_view(), name='datatype'),
    path('custom/', CUSTOMView.as_view(), name='custom'),
    path('dashboard/', DASHBOARDView.as_view(), name='dashboard'),
     path('test/', TestView.as_view(), name='test_page'),

    
]
