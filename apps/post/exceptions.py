from rest_framework.exceptions import APIException


class MessageNotExistsException(APIException):
    status_code = 404
    default_detail = 'This message does not exist.'
    default_code = 'message_not_exists'
