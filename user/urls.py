from django.urls import path,re_path
from user import views
from django.contrib.auth.views import logout_then_login

app_name='user'
urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/",  views.signout, name="logout"),
    path("profile/",  views.get_user_profile, name="profile"),
]