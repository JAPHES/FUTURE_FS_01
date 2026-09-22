import json

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .services import SERVICES, SERVICES_BY_SLUG


def home(request):
    return render(request, "techie/index.html", {"services": SERVICES})


def portfolio_details(request):
    return redirect(f"{reverse('techie:home')}#projects", permanent=True)


def service_detail(request, slug):
    service = SERVICES_BY_SLUG.get(slug)
    if service is None:
        raise Http404("Service not found")

    canonical_url = f"{settings.CANONICAL_SITE_URL}{reverse('techie:service_detail', args=[slug])}"
    structured_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{canonical_url}#service",
                "name": service["name"],
                "serviceType": service["name"],
                "description": service["meta_description"],
                "url": canonical_url,
                "provider": {
                    "@type": "Person",
                    "@id": f"{settings.CANONICAL_SITE_URL}/#person",
                    "name": "Japhes Murithi",
                    "alternateName": "Japhes",
                    "givenName": "Japhes",
                    "familyName": "Murithi",
                    "url": f"{settings.CANONICAL_SITE_URL}/",
                    "sameAs": [
                        "https://github.com/JAPHES",
                        "https://www.linkedin.com/in/japhes-murithi-79178a329",
                        "https://x.com/JaphesMurithi",
                    ],
                },
                "areaServed": {
                    "@type": "Country",
                    "name": "Kenya",
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{settings.CANONICAL_SITE_URL}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Services",
                        "item": f"{settings.CANONICAL_SITE_URL}/#services",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": service["name"],
                        "item": canonical_url,
                    },
                ],
            },
        ],
    }
    context = {
        "service": service,
        "services": SERVICES,
        "canonical_url": canonical_url,
        "structured_data": json.dumps(structured_data, ensure_ascii=False),
    }
    return render(request, "techie/service-details.html", context)


def service_details(request):
    """Preserve the old public URL while consolidating it into a useful service page."""
    return redirect(
        "techie:service_detail",
        slug="web-application-development",
        permanent=True,
    )


def starter_page(request):
    return redirect(f"{reverse('techie:home')}#about", permanent=True)


def certificates(request):
    return render(request, "techie/certificates.html")


def robots_txt(request):
    content = "\n".join([
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {settings.CANONICAL_SITE_URL}/sitemap.xml",
    ])
    return HttpResponse(content, content_type="text/plain")
