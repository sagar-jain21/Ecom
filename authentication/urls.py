from django.urls import path
from authentication.views import (
    RegisterView,
    HomeView,
    LoginView,
    LogoutView,
    DefaultView,
    )

app_name = 'authentication'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name="signup"),
    path('home/', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', DefaultView.as_view(), name="default"),
]
