import json
import re
from xml.etree import ElementTree

from django.test import SimpleTestCase, override_settings
from django.urls import reverse

from .services import SERVICES


class SeoTests(SimpleTestCase):
    request_options = {"HTTP_HOST": "localhost"}

    def test_home_has_search_and_social_metadata(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "<title>Japhes Murithi | Full-Stack Developer in Kenya</title>",
            html=True,
        )
        self.assertContains(
            response,
            '<link rel="canonical" href="https://japhes.secora.dev/">',
            html=True,
        )
        self.assertContains(response, 'name="robots" content="index, follow, max-image-preview:large"')
        self.assertNotContains(response, 'name="keywords"')

        structured_data = self._structured_data(response.content.decode())
        graph_types = {node["@type"] for node in structured_data["@graph"]}
        self.assertTrue({"ProfilePage", "Person", "WebSite", "Service"}.issubset(graph_types))

        person = next(node for node in structured_data["@graph"] if node["@type"] == "Person")
        self.assertEqual(person["name"], "Japhes Murithi")
        self.assertEqual(person["alternateName"], "Japhes")
        self.assertEqual(person["givenName"], "Japhes")
        self.assertEqual(person["familyName"], "Murithi")

        website = next(node for node in structured_data["@graph"] if node["@type"] == "WebSite")
        self.assertEqual(website["alternateName"], "Japhes Murithi Portfolio")

    def test_about_uses_coding_workspace_image(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'alt="Developer workspace with code displayed across two monitors"',
        )
        self.assertContains(response, "Building Practical Solutions")
        self.assertContains(
            response,
            "Building practical technology and stronger communities.",
        )
        self.assertContains(response, "full-stack developer, community builder, and aspiring entrepreneur")
        self.assertContains(response, "technology, innovation, and entrepreneurship")
        self.assertContains(response, "Full-Stack Development")
        self.assertContains(response, "Community Building")
        self.assertRegex(
            content,
            r"/static/techie/assets/img/about-coding-workspace(?:\.[0-9a-f]+)?\.png",
        )

    def test_home_omits_unused_frontend_dependencies(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        for unused_dependency in (
            "glightbox",
            "imagesloaded",
            "isotope-layout",
            "swiper",
            "waypoints",
        ):
            self.assertNotContains(response, unused_dependency)

    def test_home_features_affordable_housing_collaboration(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Affordable Housing Price Estimator")
        self.assertContains(response, "AI model trained by data analyst Clinton Munene")
        self.assertContains(response, "dashboard and web application built by Japhes Murithi")
        self.assertContains(response, "Need a data analyst?")
        self.assertContains(response, 'href="https://clinton-analyst.web.app/"')
        self.assertContains(response, "Explore Clinton Munene's portfolio")
        self.assertNotContains(response, "clintonmunene2000@gmail.com")
        self.assertContains(
            response,
            "https://affordable-housing-price-estimator.vercel.app/",
        )
        self.assertContains(
            response,
            "https://github.com/JAPHES/Affordable-housing-price-estimator",
        )
        self.assertRegex(
            response.content.decode(),
            r"/static/techie/assets/img/portfolio/affordable-housing-estimator(?:\.[0-9a-f]+)?\.png",
        )

    def test_universal_partnership_project_uses_current_live_url(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertRegex(
            content,
            r'(?s)Universal Partnership Association.*?href="https://jaredetaba\.secora\.dev/"',
        )
        self.assertNotContains(response, "https://uppaweb-production.up.railway.app/")

    def test_service_card_navigation_is_temporarily_hidden(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'class="service-link"')
        self.assertNotContains(response, "View service")
        self.assertNotContains(response, "<h3><a href=")

        for service_slug in (
            "web-application-development",
            "ui-ux-design",
            "mentorship-training",
            "backend-api-development",
            "iot-projects",
        ):
            self.assertContains(response, f"service-item--{service_slug}", count=1)

    def test_resume_includes_aws_leadership_and_completed_alx_course(self):
        response = self.client.get(reverse("techie:home"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AWS Student Builder Group Leader")
        self.assertContains(response, "Amazon Web Services (AWS) · Taita Taveta University")
        self.assertContains(response, "AWS Skill Builder learning paths")
        self.assertContains(response, "student project showcases")
        self.assertContains(response, "February 2026 - September 2026")
        self.assertContains(response, 'class="resume-column-content"', count=2)
        self.assertContains(response, 'class="resume-toggle"', count=2)
        self.assertContains(response, 'aria-expanded="false"', count=2)

    def test_each_service_has_unique_metadata_content_and_structured_data(self):
        titles = set()
        descriptions = set()

        for service in SERVICES:
            with self.subTest(service=service["slug"]):
                path = reverse("techie:service_detail", args=[service["slug"]])
                response = self.client.get(path, **self.request_options)
                html = response.content.decode()
                canonical_url = f"https://japhes.secora.dev{path}"

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f"<title>{service['page_title']}</title>", html=True)
                self.assertContains(response, f'<link rel="canonical" href="{canonical_url}">', html=True)
                self.assertContains(response, f"<h1>{service['name']}</h1>", html=True)
                self.assertContains(response, service["ideal_for"])
                self.assertNotContains(response, 'name="keywords"')

                structured_data = self._structured_data(html)
                service_node = next(
                    node for node in structured_data["@graph"] if node["@type"] == "Service"
                )
                self.assertEqual(service_node["url"], canonical_url)
                self.assertEqual(service_node["provider"]["name"], "Japhes Murithi")
                self.assertEqual(service_node["provider"]["alternateName"], "Japhes")
                self.assertEqual(service_node["provider"]["givenName"], "Japhes")
                self.assertEqual(service_node["provider"]["familyName"], "Murithi")

                titles.add(service["page_title"])
                descriptions.add(service["meta_description"])

        self.assertEqual(len(titles), len(SERVICES))
        self.assertEqual(len(descriptions), len(SERVICES))

    def test_sitemap_contains_only_canonical_home_and_service_urls(self):
        response = self.client.get(reverse("techie:sitemap"), **self.request_options)
        root = ElementTree.fromstring(response.content)
        namespace = {"sitemap": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = {
            element.text for element in root.findall("sitemap:url/sitemap:loc", namespace)
        }
        expected_locations = {"https://japhes.secora.dev/"}
        expected_locations.update(
            f"https://japhes.secora.dev{reverse('techie:service_detail', args=[service['slug']])}"
            for service in SERVICES
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(locations, expected_locations)
        self.assertNotIn("https://japhes.secora.dev/service-details/", locations)

    def test_robots_file_points_to_the_canonical_sitemap(self):
        response = self.client.get(reverse("techie:robots_txt"), **self.request_options)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "User-agent: *")
        self.assertContains(response, "Allow: /")
        self.assertContains(response, "Sitemap: https://japhes.secora.dev/sitemap.xml")

    def test_legacy_service_url_redirects_and_unknown_service_is_not_found(self):
        legacy_response = self.client.get(
            reverse("techie:service_details"), **self.request_options
        )
        missing_response = self.client.get(
            reverse("techie:service_detail", args=["unknown-service"]),
            **self.request_options,
        )

        self.assertRedirects(
            legacy_response,
            reverse("techie:service_detail", args=["web-application-development"]),
            status_code=301,
            fetch_redirect_response=False,
        )
        self.assertEqual(missing_response.status_code, 404)

    def test_legacy_placeholder_urls_redirect_to_relevant_home_sections(self):
        destinations = {
            "techie:portfolio_details": "/#projects",
            "techie:starter_page": "/#about",
        }

        for route_name, destination in destinations.items():
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name), **self.request_options)

                self.assertEqual(response.status_code, 301)
                self.assertEqual(response["Location"], destination)

    @override_settings(
        DEBUG=False,
        ALLOWED_HOSTS=["japhestech.vercel.app", "japhes.secora.dev"],
    )
    def test_production_alias_redirects_to_canonical_domain(self):
        alias_response = self.client.get(
            "/services/iot-projects/?source=vercel",
            HTTP_HOST="japhestech.vercel.app",
        )
        canonical_response = self.client.get("/", HTTP_HOST="japhes.secora.dev")

        self.assertEqual(alias_response.status_code, 301)
        self.assertEqual(
            alias_response["Location"],
            "https://japhes.secora.dev/services/iot-projects/?source=vercel",
        )
        self.assertEqual(canonical_response.status_code, 200)

    @staticmethod
    def _structured_data(html):
        match = re.search(
            r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
            html,
            re.DOTALL,
        )
        if match is None:
            raise AssertionError("No JSON-LD structured data was found")
        return json.loads(match.group(1))
