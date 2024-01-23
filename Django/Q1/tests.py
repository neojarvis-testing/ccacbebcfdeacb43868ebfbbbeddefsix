from django.test import TestCase
from django.urls import reverse
from django.conf import settings
import sys
import django
import json

class ServerInfoViewTest(TestCase):
    def run_test(self, test_name, func):
        try:
            func()
            print(f"Passed {test_name}")
        except AssertionError as e:
            print(f"Failed {test_name}")
            self.fail(f"Test {test_name} failed {e}")

    def test_server_info_view_status_code(self):
        url = reverse('server_info')
        response = self.client.get(url)
        self.run_test("test_server_info_view_status_code", lambda: self.assertEqual(response.status_code, 200))

    def test_server_info_view_content(self):
        url = reverse('server_info')
        response = self.client.get(url)
        self.run_test("test_server_info_view_content", lambda: self.assertContains(response, 'django_version'))

    def test_server_info_view_json_response(self):
        url = reverse('server_info')
        response = self.client.get(url)

        django_version = django.get_version()
        python_version = sys.version
        debug_mode = settings.DEBUG

        expected_response_data = {
            'django_version': django_version,
            'python_version': python_version,
            'debug_mode': debug_mode,
        }

        self.run_test("test_server_info_view_json_response", lambda: self.assertJSONEqual(response.content, expected_response_data))

    def test_server_info_view_with_debug_off(self):
        # Test the view when DEBUG mode is turned off
        with self.settings(DEBUG=False):
            url = reverse('server_info')
            response = self.client.get(url)
            self.run_test("test_server_info_view_with_debug_off", lambda: self.assertContains(response, '"debug_mode": false'))
