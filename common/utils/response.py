from rest_framework import status
from rest_framework.response import Response

RESPONSE_CODE_DICT = {
    200: {
        "success": True,
        "message": "SUCCESS",
        "status": status.HTTP_200_OK,
    },
    401: {
        "success": False,
        "message": "UNAUTHORIZED",
        "status": status.HTTP_401_UNAUTHORIZED,
    },
}


class JsonResponseGenerator:
    @staticmethod
    def create_response(code, data={}):
        code_info = RESPONSE_CODE_DICT.get(
            code,
            {
                "success": False,
                "message": "UNKNOWN",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
        )
        response_data = {
            "code": code,
            "success": code_info["success"],
            "message": code_info["message"],
            "data": data,
        }
        return Response(response_data, status=code_info["status"])
