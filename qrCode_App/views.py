from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base.html'



# custom views for error pages
def custom_page_not_found_view(request, exception):
    return render(request, "404.html")

def custom_error_view(request, exception=None):
    return render(request, "404.html")

def custom_permission_denied_view(request, exception=None):
    return render(request, "404.html")

def custom_bad_request_view(request, exception=None):
    return render(request, "404.html")