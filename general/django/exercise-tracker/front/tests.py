from django.test import TestCase
from django.urls import reverse


class FileMetaDataFrontViewTest(TestCase):
    def test_template_title(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "<title>Exercise Tracker</title>", status_code=200)

    def test_template_form_name_user(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "Create User", status_code=200)

    def test_template_form_name_exercise(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, "Add Exercises", status_code=200)

    def test_template_form_user(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, 'action="/api/users"', status_code=200)

    def test_template_form_exercise(self):
        resp = self.client.get(reverse("index"))
        self.assertContains(resp, 'id="exercise-form"', status_code=200)
