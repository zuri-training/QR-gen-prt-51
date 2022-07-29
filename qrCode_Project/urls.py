from django.contrib import admin
from django.conf.urls import handler400, handler403,handler404,handler500
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='components/landingPage.html'), name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include('qrCode_App.urls')),
]

# views for custom error page
handler404 = 'qrCode_App.views.custom_page_not_found_view'
handler500 = 'qrCode_App.views.custom_error_view'
handler403 = 'qrCode_App.views.custom_permission_denied_view'
handler400 = 'qrCode_App.views.custom_bad_request_view'