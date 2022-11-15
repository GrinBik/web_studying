from django.test import Client, TestCase
from django.urls import reverse


class TestCases(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_main_page_status_code(self):
        response = self.client.get(reverse("greeting"))
        self.assertEqual(response.status_code, 200)

    def test_biography_page_status_code(self):
        response = self.client.get(reverse("biography"))
        self.assertEqual(response.status_code, 200)

    def test_project_page_status_code(self):
        response = self.client.get("/project/?dir=.")
        self.assertEqual(response.status_code, 200)
