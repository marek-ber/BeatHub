from django.urls import path
from .views import profile_view, edit_profile, register_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("edit/", edit_profile, name="edit_profile"),
    path("<str:username>/", profile_view, name="profile"),
]