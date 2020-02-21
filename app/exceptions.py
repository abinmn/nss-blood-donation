from typing import List
from rest_framework.exceptions import APIException


class QueryParameterRequiredException(APIException):
    """Exception to raise if required query parameter is not passed.

    :param fields: A list of required fields
    """

    status_code = 400
    default_code = 'parameter_required'

    def __init__(self,fields: List, detail=None, code=None):
        detail = f'Query parameters not found: {fields}'
        super().__init__(detail=detail, code=code)
