class APIException(Exception):
    '''General unexpected response'''
    pass


class InvalidAppId(APIException):
    '''Invalid key, HTTP 401'''
    pass