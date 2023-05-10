from django.test import TestCase


# Create your tests here.
class SimpleTest1(TestCase):
    def test1(self):
        response = self.client.get('/depart/list')
        self.assertEqual(response.status_code, 200)
