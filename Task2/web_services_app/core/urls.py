from django.contrib import admin
from django.urls import include, path

from .views import HealthCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/app/", include("web_app.urls")),
    path("", HealthCheckView.as_view(), name="health-check"),
]
