from django.urls import path
from .views import (
    signup_view, LoginViewCustom, LogoutViewCustom,
    profile_view, profile_edit, PasswordChangeViewCustom
)

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutViewCustom.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/editar/', profile_edit, name='profile_edit'),
    path('password-change/', PasswordChangeViewCustom.as_view(), name='password_change'),
]
