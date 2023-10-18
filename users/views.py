from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from common.utils.response import JsonResponseGenerator


class UserLogin(APIView):
    """
    사용자 로그인을 처리하는 API

    POST 로그인
    """

    @swagger_auto_schema(
        operation_summary="유저 로그인 api",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "code": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                        ),
                        "success": openapi.Schema(
                            type=openapi.TYPE_BOOLEAN,
                        ),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "data": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "access_token": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                                "refresh_token": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                ),
                            },
                        ),
                    },
                ),
                examples={
                    "application/json": {
                        "code": 200,
                        "success": True,
                        "message": "SUCCESS",
                        "data": {
                            "access_token": "access_token",
                            "refresh_token": "refresh_token",
                        },
                    }
                },
            ),
            401: openapi.Response(
                description="Unauthorized response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "code": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                        ),
                        "success": openapi.Schema(
                            type=openapi.TYPE_BOOLEAN,
                        ),
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "data": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                        ),
                    },
                ),
                examples={
                    "application/json": {
                        "code": 401,
                        "success": False,
                        "message": "UNAUTHORIZED",
                        "data": {},
                    }
                },
            ),
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="유저 id (email)",
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="유저 비밀번호",
                ),
            },
        ),
    )
    def post(self, request):
        user = authenticate(request, **request.data)

        if user:
            refresh_token = RefreshToken.for_user(user)
            data = {
                "access_token": str(refresh_token.access_token),
                "refresh_token": str(refresh_token),
            }
            return JsonResponseGenerator.create_response(
                code=200,
                data=data,
            )
        else:
            return JsonResponseGenerator.create_response(code=401)


class UserSignUp(APIView):
    """
    사용자 회원기입을 처리하는 API

    POST 회원가입
    """

    def post(self, request):
        pass


class UserLogOut(APIView):
    """
    사용자 로그아웃 API

    POST 로그아웃
    """

    def post(self, request):
        pass
