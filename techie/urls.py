from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import StaticViewSitemap

app_name = "techie"

urlpatterns = [
    path("", views.home, name="home"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"static": StaticViewSitemap}},
        name="sitemap",
    ),
    path("certificates/", views.certificates, name="certificates"),
    path("portfolio-details/", views.portfolio_details, name="portfolio_details"),
    path("service-details/", views.service_details, name="service_details"),
    path("starter-page/", views.starter_page, name="starter_page"),
]
