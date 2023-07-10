from django.test import TestCase
from django.urls import reverse


class WhoamiViewTest(TestCase):
    def test_view_url_whoami(self):
        resp = self.client.get(
            reverse("whoami"),
            **{
                "HTTP_USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64)",
                "HTTP_ACCEPT_LANGUAGE": "en-US,en;q=0.9,es;q=0.8",
                "REMOTE_ADDR": "127.0.0.1",
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_view_whoami_fields(self):
        resp = self.client.get(
            reverse("whoami"),
            **{
                "HTTP_USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64)",
                "HTTP_ACCEPT_LANGUAGE": "en-US,en;q=0.9,es;q=0.8",
                "REMOTE_ADDR": "127.0.0.1",
            }
        )
        self.assertEqual(
            resp.json(),
            {
                "software": "Mozilla/5.0 (X11; Linux x86_64)",
                "language": "en-US,en;q=0.9,es;q=0.8",
                "ipaddress": "127.0.0.1",
            },
        )
