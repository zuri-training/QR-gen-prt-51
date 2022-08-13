
from django.urls import path
from . import views
from .views import contact
from .views import LandingPageView,CONTACTPageView,FAQPageView,ABOUTPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('contact/', contact,  name='contact-us'),
    path('contact/',views.contact, name='contact-us'),
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
    path('datatype/predefined-message', views.predefined_message, name='predefined-message'),
    path('resetall', views.resetall, name='resetall'),
    path('code/<int:pk>', views.code_detail, name='code_detail'),
    path('code/<int:pk>/download_png', views.code_download_png, name='code_download_png'),
    path('code/<int:pk>/download_svg', views.code_download_svg, name='code_download_svg'),
    path('code/<int:pk>/download_jpeg', views.code_download_jpeg, name='code_download_jpeg'),
    path('code/<int:pk>/download_pdf', views.code_download_pdf, name='code_download_pdf'),
    path('code/<int:pk>/edit', views.code_edit, name='code_edit'),
]
