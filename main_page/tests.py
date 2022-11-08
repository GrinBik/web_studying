from django.test import Client, 	TestCase

class IndexTestCase(TestCase):
	def setUp(self) -> None:
		self.client = Client()

	def test_get_index(self):
		response = self.client.get("/")
		self.asserEqual(response.status_code, 200)