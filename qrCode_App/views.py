from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "components/landingPage.html"
class FAQPageView(TemplateView):
    template_name = 'components/faq.html'
class CONTACTPageView(TemplateView):
    template_name = 'components/contactus.html'
class ABOUTPageView(TemplateView):
    template_name = 'components/aboutus.html'
class DATAPageview(TemplateView):
    template_name = 'components/datatype.html'
    
    
# custom views for error pages
def custom_page_not_found_view(request, exception):
    return render(request, "404.html")

def custom_error_view(request, exception=None):
    return render(request, "404.html")

def custom_permission_denied_view(request, exception=None):
    return render(request, "404.html")

def custom_bad_request_view(request, exception=None):
    return render(request, "404.html")