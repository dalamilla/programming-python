from base64 import b64decode
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class FileMetaDataApiAnalyseViewTest(TestCase):
    def test_fileanalyse_txt(self):
        content = b"txt test file\n"
        file = SimpleUploadedFile("test.txt", content, content_type="text/plain")
        resp = self.client.post(reverse("fileanalyse"), {"upfile": file})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(), {"name": "test.txt", "size": "14", "type": "text/plain"}
        )

    def test_fileanalyse_json(self):
        content = b'{\n    "description": "json test file"\n}'
        file = SimpleUploadedFile("test.json", content, content_type="application/json")
        resp = self.client.post(reverse("fileanalyse"), {"upfile": file})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "name": "test.json",
                "size": "39",
                "type": "application/json",
            },
        )

    def test_fileanalyse_img(self):
        content = b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAw"
            "CAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
        )
        file = SimpleUploadedFile("test.png", content, content_type="image/png")
        resp = self.client.post(reverse("fileanalyse"), {"upfile": file})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(), {"name": "test.png", "size": "68", "type": "image/png"}
        )
