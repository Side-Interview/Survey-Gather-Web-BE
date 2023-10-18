from config.env import env

SWAGGER_ENABLED = env.bool("SWAGGER_ENABLED", default=True)
SWAGGER_SETTINGS = {
    # "SECURITY_DEFINITIONS": {
    #     "JWT [Bearer {JWT}]": {
    #         "name": "Authorization",
    #         "type": "apiKey",
    #         "in": "header",
    #     }
    # },
    # TODO: 필요시 해당 Header 로 사용
    #     manual_parameters=[
    #     openapi.Parameter(
    #         name="Authorization",
    #         in_=openapi.IN_HEADER,
    #         type=openapi.TYPE_STRING,
    #         description="JWT 토큰 (Bearer {JWT})",
    #         required=True,
    #     ),
    # ],
    "USE_SESSION_AUTH": False,
}
