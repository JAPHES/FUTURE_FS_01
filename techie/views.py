from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "techie/index.html")


def portfolio_details(request):
    return render(request, "techie/portfolio-details.html")


def service_details(request):
    return render(request, "techie/service-details.html")


def starter_page(request):
    return render(request, "techie/starter-page.html")


def certificates(request):
    return render(request, "techie/certificates.html")


def robots_txt(request):
    content = "\n".join([
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://japhes.secora.dev/sitemap.xml",
    ])
    return HttpResponse(content, content_type="text/plain")
