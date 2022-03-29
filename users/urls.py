from django.urls import path
import users.views

app_name = 'users'

urlpatterns = [
    path('login/', users.views.IndexView.as_view(), name='login'),
]