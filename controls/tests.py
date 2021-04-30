import unittest

from django.test import TestCase, Client


class SimpleTest(TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/controls/')
        # self.assertEqual(response.status_code, 200)