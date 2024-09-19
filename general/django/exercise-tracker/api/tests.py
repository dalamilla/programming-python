import json
from urllib.parse import urlencode

from django.test import TestCase
from django.urls import reverse


class ExerciseTrackerViewTest(TestCase):
    def test_get_users(self):
        resp = self.client.get(reverse("users"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), [])

    def test_post_jsonparser_create_user(self):
        data = {"username": "alex"}
        resp = self.client.post(
            reverse("users"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("username"), "alex")

    def test_post_formparser_create_user(self):
        data = urlencode({"username": "andy"})
        resp = self.client.post(
            reverse("users"), data, "application/x-www-form-urlencoded"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("username"), "andy")

    def test_get_user_empty_logs(self):
        data = urlencode({"username": "matt"})
        post = self.client.post(
            reverse("users"), data, "application/x-www-form-urlencoded"
        )
        username_id = post.json().get("_id")
        resp = self.client.get(reverse("logs", kwargs={"username_id": username_id}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("log"), [])

    def test_post_jsonparser_user_create_exercises(self):
        data = {"username": "jamie"}
        post_u = self.client.post(
            reverse("users"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        username_id = post_u.json().get("_id")
        data = {"description": "run day", "duration": 60, "date": "2021-01-11"}
        post_ex = self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(post_ex.status_code, 200)
        self.assertEqual(
            post_ex.json(),
            {
                "_id": username_id,
                "description": "run day",
                "duration": 60,
                "date": "Mon Jan 11 2021",
                "username": "jamie",
            },
        )

    def test_get_user_logs(self):
        data = {"username": "nick"}
        post_u = self.client.post(
            reverse("users"),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        username_id = post_u.json().get("_id")
        data = {"description": "run day", "duration": 60, "date": "2021-02-10"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "jump day", "duration": 60, "date": "2021-02-11"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "run day", "duration": 60, "date": "2021-02-12"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "jump day", "duration": 60, "date": "2021-02-13"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "run day", "duration": 60, "date": "2021-02-14"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "jump day", "duration": 60, "date": "2021-02-14"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "run day", "duration": 60, "date": "2021-02-15"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        data = {"description": "jump day", "duration": 60, "date": "2021-02-16"}
        self.client.post(
            reverse("exercises", kwargs={"username_id": username_id}),
            json.dumps(data),
            "application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        limit_q = self.client.get(
            reverse("logs", kwargs={"username_id": username_id}), {"limit": "2"}
        )
        from_q = self.client.get(
            reverse("logs", kwargs={"username_id": username_id}), {"from": "2021-02-13"}
        )
        to_q = self.client.get(
            reverse("logs", kwargs={"username_id": username_id}), {"to": "2021-02-15"}
        )
        from_to_q = self.client.get(
            reverse("logs", kwargs={"username_id": username_id}),
            {"from": "2021-02-11", "to": "2021-02-14"},
        )

        self.assertEqual(len(limit_q.json().get("log")), 2)
        self.assertEqual(len(from_q.json().get("log")), 5)
        self.assertEqual(len(to_q.json().get("log")), 7)
        self.assertEqual(len(from_to_q.json().get("log")), 5)
