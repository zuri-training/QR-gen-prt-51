from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from qrApi import views
from django.conf.urls import handler400, handler403, handler404, handler500

# schema view
schema_view = get_schema_view(
    openapi.Info(
        title="QR_GENERATION DOCS",
        default_version="v1",
        description="Generate and personalized qrcode, zuri project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="petsamuel4@gmail.com"),
        license=openapi.License(name="TEAM-51 License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("qrCode_App.urls")),
    path("", TemplateView.as_view(template_name="pages/landingPage.html"), name="home"),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("api/", include("qrApi.urls")),
    path("auth/", obtain_auth_token, name="Api_token"),
    path("api.test", views.TestViewSet.as_view(), name="testApi"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# views for custom error page
handler404 = "qrCode_App.views.custom_page_not_found_view"
handler500 = "qrCode_App.views.custom_error_view"
handler403 = "qrCode_App.views.custom_permission_denied_view"
handler400 = "qrCode_App.views.custom_bad_request_view"
