from datetime import datetime, timezone

from django.test import TestCase
from django.urls import reverse


class DateViewTest(TestCase):
    def test_view_date(self):
        resp = self.client.get(reverse("date", args=["2016-12-25"]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "unix": 1482624000000,
                "utc": "Sun, 25 Dec 2016 00:00:00 GMT",
            },
        )

    def test_view_date_epoch(self):
        resp = self.client.get(reverse("date", args=["1451001600000"]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "unix": 1451001600000,
                "utc": "Fri, 25 Dec 2015 00:00:00 GMT",
            },
        )

    def test_view_date_with_space(self):
        resp = self.client.get(reverse("date", args=["05 October 2011"]))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "unix": 1317772800000,
                "utc": "Wed, 05 Oct 2011 00:00:00 GMT",
            },
        )

    def test_view_date_with_space_and_timezone(self):
        resp = self.client.get(reverse("date", args=["05 October 2011, GMT"]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "unix": 1317772800000,
                "utc": "Wed, 05 Oct 2011 00:00:00 GMT",
            },
        )

    def test_view_date_no_a_date(self):
        resp = self.client.get(reverse("date", args=["this-is-not-a-date"]))
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.json(),
            {"error": "Invalid Date"},
        )

    def test_view_date_now(self):
        current = datetime.now(timezone.utc)
        unix = int(current.timestamp() * 1000)
        utc = current.strftime("%a, %d %b %Y %H:%M:%S GMT")

        resp = self.client.get(reverse("date", args=[unix]))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "unix": unix,
                "utc": utc,
            },
        )

    def test_view_date_no_parameter(self):
        current = datetime.now(timezone.utc)
        unix = int(current.timestamp())
        utc = current.strftime("%a, %d %b %Y %H:%M:%S GMT")

        resp = self.client.get(reverse("date"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("utc"), utc)
        self.assertEqual(int(resp.json().get("unix") / 1000), unix)
