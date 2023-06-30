"""Lifestyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path,re_path
from  django.conf.urls import handler404,handler500

from Blog.sitemaps import BlogSitemap

sitemaps = {
    "blogs": BlogSitemap,
}

urlpatterns = [
    path("admin/defender/", include("defender.urls")),  # defender admin
    path('hijack/', include('hijack.urls')),
    path('admin/', include('admin_honeypot.urls')),
    path("allowmepass/", admin.site.urls),
    path("blogs/", include("Blog.urls")),
    path("", include("Pages.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("profile/", include("Accounts.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("accounts/", include("allauth.urls")),
    path("hitcount/", include(("hitcount.urls", "hitcount"), namespace="hitcount")),
    re_path(r"^maintenance-mode/", include("maintenance_mode.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = 'Pages.views.error_404'
handler500 = 'Pages.views.error_500'
