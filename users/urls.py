from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="Login"),
    path("signup/", views.UserSignUp.as_view(), name="Sign Up"),
    path("logout/", views.UserLogOut.as_view(), name="Logout"),
    # 추가로 작성해야 할 API LIST - 추가 및 삭제가 필요할 수도
    # path("logout/", views.LogOut.as_view()),
    # path("me/", views.UserMe.as_view()),
    # path("checkID/", views.CheckID.as_view()),
    # path("changepassword/", views.ChangePassword.as_view()),
    # path("find/id", views.FindId.as_view()),
    # path("find/password", views.FindPassword.as_view()),
    # path("new-password", views.NewPassword.as_view()),
]
