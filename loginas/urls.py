from django.urls import path

from loginas.views import user_login, user_login2
from loginas.views import user_logout

urlpatterns = [
    path("login/user/", user_login2, name="loginas-user"),
    path("login/user/<str:user_id>/", user_login, name="loginas-user-login"),
    path("logout/", user_logout, name="loginas-logout"),
]
