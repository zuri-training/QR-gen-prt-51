
from django.urls import path
from .views import (HomePageView, ContactUsView)
urlpatterns = [
    path('', HomePageView.as_view(), name='Index'),
    path('/contactus', ContactUsView.as_view(), name='contact-us')
]
