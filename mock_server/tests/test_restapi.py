# -*- coding: utf-8 -*-

import os

import tornado.testing
from mock_server.server import Application


class TestRestApi(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        return Application(7777, "localhost",
                           os.path.join(os.path.dirname(__file__), "api/"),
                           False, "application.json")

    def test_list_users(self):
        response = self.fetch("/user")

        self.assertFalse(response.error)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, '["john", "tom"]\n')

    def test_user_doesnt_exists_with_custom_header(self):
        response = self.fetch("/user/tom?__statusCode=404")

        self.assertEqual(response.code, 404)
        self.assertEqual(response.body,
                         '{"message": "User doesn\'t exists"}\n')
        self.assertEqual(response.headers["MyCustomHeader"], "test")

    def test_noexists_method(self):
        response = self.fetch("/user/john/data")

        self.assertEqual(response.code, 404)
        self.assertEqual(
            response.body,
            'Api does\'t exists, '
            '<a href="/__manage/create?url_path=user/'
            'john/data&method=GET&status_code=200&format=json">'
            'create resource method</a>')

    def test_url_with_variables(self):
        response = self.fetch("/user/lisa/family/bart")

        self.assertEqual(response.code, 200)
        self.assertTrue("bart" in response.body)
