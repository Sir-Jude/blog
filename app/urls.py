"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('app/', include('app.urls'))
"""

import os
from dotenv import load_dotenv
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import include, path
from blog.views import HomeView, custom_upload_function

load_dotenv()

urlpatterns = [
    path(os.getenv("ADMIN_URL", "admin/"), admin.site.urls),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico")),
    ),
    path("", HomeView.as_view(), name="home"),
    path("blog/", include("blog.urls")),
    path("registration/", include("django.contrib.auth.urls")),
    path("registration/", include("registration.urls")),
    path("upload/", custom_upload_function, name="custom_upload_file"),
]

urlpatterns += staticfiles_urlpatterns()

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.TESTING:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
