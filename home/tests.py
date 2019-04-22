from django.shortcuts import resolve_url
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.page_url = resolve_url("home:index")

    def test_url(self):
        self.assertEqual(self.page_url, "/")

    def test_status_code_200(self):
        res = self.client.get(self.page_url)
        self.assertEqual(res.status_code, 200)

    def test_title(self):
        res = self.client.get(self.page_url)
        self.assertContains(res, 'Azure DevOps 배포 데모')

