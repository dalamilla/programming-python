from django.test import TestCase
from django.urls import reverse


class FileMetaDataFrontViewTest(TestCase):
    def test_template_title(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "<title>Form File</title>", status_code=200)

    def test_template_form_name(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, 'name="upfile"', status_code=200)

    def test_template_form_action(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, 'action="/api/fileanalyse"', status_code=200)
