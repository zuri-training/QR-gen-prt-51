
from django.urls import path
from . import views
from .views import LandingPageView, CONTACTPageView, FAQPageView, ABOUTPageView,
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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/', views.success, name='success'),
    path('datatype/popular', views.popular, name='popular'),
    path('datatype/social-links', views.social_links, name='social-links'),
    path('datatype/business-links', views.business_links, name='business-links'),
    path('datatype/predefined-message',
         views.predefined_message, name='predefined-message'),
    path('resetall', views.resetall, name='resetall'),


]
