import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.question import Question  # noqa: E501
from openapi_server import util


def delete_question(survey_id, question_id):  # noqa: E501
    """Delete Question

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param question_id: 
    :type question_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_question(survey_id, question_id):  # noqa: E501
    """Get Question

     # noqa: E501

    :param survey_id: 
    :type survey_id: int
    :param question_id: 
    :type question_id: int

    :rtype: Union[Question, Tuple[Question, int], Tuple[Question, int, Dict[str, str]]
    """
    return 'do some magic!'
