from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("sprawozdania/", include("sprawozdania.urls")),
    path("admin/", admin.site.urls),
]