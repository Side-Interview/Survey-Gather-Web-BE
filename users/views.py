from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from common.utils.response import JsonResponseGenerator


class UserLogin(APIView):
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
