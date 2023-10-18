from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="Login"),
    # 추가로 작성해야 할 API LIST - 추가 및 삭제가 필요할 수도
    # path("signup/", views.SignUp.as_view()),
    # path("logout/", views.LogOut.as_view()),
    # path("me/", views.UserMe.as_view()),
    # path("checkID/", views.CheckID.as_view()),
    # path("logout/", views.LogOut.as_view()),
    # path("changepassword/", views.ChangePassword.as_view()),
    # path("find/id", views.FindId.as_view()),
    # path("find/password", views.FindPassword.as_view()),
    # path("new-password", views.NewPassword.as_view()),
]
