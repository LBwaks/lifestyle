from django.contrib.sitemaps.views import sitemap
from django.urls import path

# from .sitemaps import StaticViewSitemap
from .views import About, ContactView, Home

# sitemaps = {
#     "static": StaticViewSitemap,
# }

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("contact", ContactView, name="contact"),
    # path(
    #     "sitemap.xml",
    #     sitemap,
    #     {"sitemaps": sitemaps},
    #     name="django.contrib.sitemaps.views.sitemap",
    # ),
]
