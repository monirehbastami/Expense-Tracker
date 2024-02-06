from django.urls import path
from users.views import UserLoginView, UserRegisterView

app_name = 'users'
urlpatterns = [
    path('', UserLoginView.as_view(), name='home'),
    path('user/register/', UserRegisterView.as_view(), name='register'),
]
