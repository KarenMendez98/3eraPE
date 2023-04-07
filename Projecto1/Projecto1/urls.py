from django.contrib import admin
from django.urls import path, include
from AppKaren.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio),
    path("AppKaren/", include("AppKaren.urls")),
]