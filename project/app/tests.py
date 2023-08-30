from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from . models import Client
from django.urls import reverse

class TestClientApiView(APITestCase):

    def setUp(self):
        self.url = reverse('cvs-file')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertAlmostEquals(200, response.status_code)

    def test_post(self):
        files = {'csv_file': open('deals.csv', 'rb')}
        response = self.client.post(self.url, data=files)
        self.assertAlmostEquals(201, response.status_code)