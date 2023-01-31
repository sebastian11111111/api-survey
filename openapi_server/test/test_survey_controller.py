# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.create_question import CreateQuestion  # noqa: E501
from openapi_server.models.create_survey import CreateSurvey  # noqa: E501
from openapi_server.models.publish import Publish  # noqa: E501
from openapi_server.models.question import Question  # noqa: E501
from openapi_server.models.questions import Questions  # noqa: E501
from openapi_server.models.set_end import SetEnd  # noqa: E501
from openapi_server.models.set_start import SetStart  # noqa: E501
from openapi_server.models.survey import Survey  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSurveyController(BaseTestCase):
    """SurveyController integration test stubs"""

    def test_create_question(self):
        """Test case for create_question

        Create Question
        """
        create_question = {"question":"question","question-type":"question-type","answers":"answers"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/question'.format(survey_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(create_question),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_survey(self):
        """Test case for create_survey

        Create Survey
        """
        create_survey = {"name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/surveys',
            method='POST',
            headers=headers,
            data=json.dumps(create_survey),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_survey(self):
        """Test case for delete_survey

        Delete Survey
        """
        headers = { 
        }
        response = self.client.open(
            '/surveys/{survey_id}'.format(survey_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_questions(self):
        """Test case for list_questions

        List Questions
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/question'.format(survey_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_publish(self):
        """Test case for publish

        Publish
        """
        publish = {"id":0}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/publish'.format(survey_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(publish),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_end(self):
        """Test case for set_end

        Set End-Date
        """
        set_end = {"end-date":"end-date","id":0}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/end_date'.format(survey_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(set_end),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_start(self):
        """Test case for set_start

        Set Start-Date
        """
        set_start = {"start-date":"start-date","id":0}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/surveys/{survey_id}/start_date'.format(survey_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(set_start),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
