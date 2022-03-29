from django.urls import path
import users.views

app_name = 'users'

urlpatterns = [
    path('login/', users.views.UserLoginView.as_view(), name='login'),
    path('logout/', users.views.UserLogoutView.as_view(), name='logout'),
    path('register/', users.views.UserRegisterView.as_view(), name='register'),
]
