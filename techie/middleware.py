from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class CanonicalHostRedirectMiddleware:
    """Consolidate the production Vercel alias into the public canonical domain."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_host = request.get_host().split(":", 1)[0].lower()
        if not settings.DEBUG and request_host == "japhestech.vercel.app":
            canonical_url = f"{settings.CANONICAL_SITE_URL}{request.get_full_path()}"
            return HttpResponsePermanentRedirect(canonical_url)

        return self.get_response(request)
