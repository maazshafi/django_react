from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", views.registerUser, name="register"),
    path("profile/", views.getUserProfile, name="users-profle"),
    path("profile/update/", views.updateUserProfile, name="user-profle-update"),
    path("", views.getUsers, name="users"),
]
