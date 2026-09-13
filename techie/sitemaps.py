from types import SimpleNamespace

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .services import SERVICES


class CanonicalSitemap(Sitemap):
    protocol = "https"

    def get_urls(self, page=1, site=None, protocol=None):
        canonical_site = SimpleNamespace(domain=settings.CANONICAL_HOST)
        return super().get_urls(page=page, site=canonical_site, protocol="https")


class StaticViewSitemap(CanonicalSitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ["techie:home"]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(CanonicalSitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return SERVICES

    def location(self, service):
        return reverse("techie:service_detail", args=[service["slug"]])
