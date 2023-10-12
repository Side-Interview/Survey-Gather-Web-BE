import logging

from django.urls import include, path

logger = logging.getLogger("configuration")


def show_toolbar(*args, **kwargs) -> bool:
    """
    일반적인 아이디어는 다음과 같습니다:

    1. toolbar 가 설치되어 있고 표시되도록 설정되어 있다면 toolbar를 표시합니다.
        - 이렇게 하면 필요하다면 종속성을 로컬로 이동하는 옵션을 열어줍니다.
    2. 이 함수는 단일 소스 역할을 합니다.
        - 다른 곳에서 추가 확인이 필요하지 않습니다.
    이것은 다음과 같은 옵션을 가능하게 합니다:

    - 프로덕션 환경에서 표시합니다
    - 프로덕션 환경에서 전체 종속성 제외합니다
    - 단일 Django 설정을 통해 디버그 toolbar를 제어할 수 있는 유연성을 갖습니다.
    """
    from config.settings.debug_toolbar.settings import DEBUG_TOOLBAR_ENABLED

    if not DEBUG_TOOLBAR_ENABLED:
        return False

    try:
        import debug_toolbar  # noqa
    except ImportError:
        logger.info("No installation found for: django_debug_toolbar")
        return False

    return True


class DebugToolbarSetup:
    @staticmethod
    def do_settings(INSTALLED_APPS, MIDDLEWARE, middleware_position=None):
        _show_toolbar: bool = show_toolbar()
        logger.info(f"Django Debug Toolbar in use: {_show_toolbar}")

        if not _show_toolbar:
            return INSTALLED_APPS, MIDDLEWARE

        INSTALLED_APPS += ["debug_toolbar"]

        # 이를 처리하기 위해:
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware
        # MIDDLEWARE 순서가 중요합니다.
        # 응답 콘텐츠를 인코딩하는 다른 미들웨어(예: GZipMiddleware)보다 Debug Toolbar 미들웨어를 먼저 포함해야 합니다.
        # 임의의 위치에 미들웨어를 삽입할 수 있습니다.
        # 위치가 지정되지 않은 경우 목록의 끝에 포함합니다.
        debug_toolbar_middleware = "debug_toolbar.middleware.DebugToolbarMiddleware"

        if middleware_position is None:
            MIDDLEWARE = MIDDLEWARE + [debug_toolbar_middleware]
        else:
            _middleware = MIDDLEWARE[::]
            _middleware.insert(middleware_position, debug_toolbar_middleware)

            MIDDLEWARE = _middleware

        return INSTALLED_APPS, MIDDLEWARE

    @staticmethod
    def do_urls(urlpatterns):
        if not show_toolbar():
            return urlpatterns

        import debug_toolbar  # noqa

        return urlpatterns + [path("__debug__/", include(debug_toolbar.urls))]
