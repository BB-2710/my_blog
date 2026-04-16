from django.urls import path
from .views import register_view, login_view, logout_view
from .views import home, create_post
from .views import edit_post, delete_post


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_post, name="create_post"),
    path("edit/<int:id>/", edit_post, name="edit_post"),
    path("delete/<int:id>/", delete_post, name="delete_post"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]