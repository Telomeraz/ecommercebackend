from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    path("api/v1/products/", include("products.api.v1.urls")),
    path("api/v1/accounts/", include("accounts.api.v1.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
