from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "pages/landingPage.html"
class FAQPageView(TemplateView):
    template_name = 'pages/faq.html'
class CONTACTPageView(TemplateView):
    template_name = 'pages/contactus.html'
class ABOUTPageView(TemplateView):
    template_name = 'pages/aboutUs.html'
class DATAPageview(TemplateView):
    template_name = 'pages/datatype.html'

class CUSTOMView(TemplateView):
    template_name = 'pages/customizeqr.html'

class DASHBOARDView(TemplateView):
    template_name = 'pages/dashboard.html'
class TestView(TemplateView):
    template_name = "components/emaillink.html"
 
# custom views for error pages
def custom_page_not_found_view(request, exception):
    return render(request, "404.html")

def custom_error_view(request, exception=None):
    return render(request, "404.html")

def custom_permission_denied_view(request, exception=None):
    return render(request, "404.html")

def custom_bad_request_view(request, exception=None):
    return render(request, "404.html")

# CBV for contact us page
class ContactUsView(TemplateView):
    template_name = 'contactus.html'