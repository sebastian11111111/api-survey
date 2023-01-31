# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.question import Question  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_delete_question(self):
        """Test case for delete_question

        Delete Question
        """
        headers = { 
        }
        response = self.client.open(
            '/surveys/{survey_id}/{question_id}'.format(survey_id=56, question_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_question(self):
        """Test case for get_question

        Get Question
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/{question_id}'.format(survey_id=56, question_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
