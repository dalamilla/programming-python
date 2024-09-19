import json
from urllib.parse import urlencode

from django.test import TestCase
from django.urls import reverse


class UrlShortenerViewTest(TestCase):
    def test_get_not_found(self):
        resp = self.client.get(reverse("shorturl", args=["100"]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(), {"error": "No short URL found for the given input"}
        )

    def test_get_incorrect_format(self):
        resp = self.client.get(reverse("shorturl", args=["text"]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"error": "Wrong format"})

    def test_post_jsonparser_invalid_url(self):
        data = {"url": "htt://example.com"}
        resp = self.client.post(
            reverse("shorturl"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"error": "Invalid url"})

    def test_post_jsonparser_invalid_hostname(self):
        data = {"url": "http://examplesss.com"}
        resp = self.client.post(
            reverse("shorturl"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"error": "Invalid Hostname"})

    def test_post_jsonparser_url(self):
        data = {"url": "https://www.freecodecamp.org/"}
        resp = self.client.post(
            reverse("shorturl"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json().get("original_url"), "https://www.freecodecamp.org/"
        )

    def test_redirect_jsonparser_url(self):
        data = {"url": "https://teachyourselfcs.com/"}
        post = self.client.post(
            reverse("shorturl"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        short_url = post.json().get("short_url")
        resp = self.client.get(reverse("shorturl", args=[short_url]))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, "https://teachyourselfcs.com/")

    def test_post_formparser_invalid_url(self):
        data = urlencode({"url": "htt://example.com"})
        resp = self.client.post(
            reverse("shorturl"), data, "application/x-www-form-urlencoded"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"error": "Invalid url"})

    def test_post_formparser_invalid_hostname(self):
        data = urlencode({"url": "http://examplesss.com"})
        resp = self.client.post(
            reverse("shorturl"), data, "application/x-www-form-urlencoded"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"error": "Invalid Hostname"})

    def test_post_formparser_url(self):
        data = urlencode({"url": "https://www.freecodecamp.org/"})
        resp = self.client.post(
            reverse("shorturl"), data, "application/x-www-form-urlencoded"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json().get("original_url"), "https://www.freecodecamp.org/"
        )

    def test_redirect_formparser_url(self):
        data = urlencode({"url": "https://teachyourselfcs.com/"})
        post = self.client.post(
            reverse("shorturl"), data, "application/x-www-form-urlencoded"
        )
        short_url = post.json().get("short_url")
        resp = self.client.get(reverse("shorturl", args=[short_url]))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, "https://teachyourselfcs.com/")
