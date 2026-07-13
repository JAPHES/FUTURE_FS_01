from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"

    def items(self):
        return ["techie:home", "techie:certificates"]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == "techie:home" else 0.7
