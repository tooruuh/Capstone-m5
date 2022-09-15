from rest_framework.exceptions import APIException, _get_error_details, status

class ValidationDuplicatedProduct(APIException):
    status_code = status.HTTP_409_CONFLICT

class ValidationIsSelled(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE