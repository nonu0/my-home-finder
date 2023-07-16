from django.urls import path
from apps.authentication.views import RegisterView

urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login',RegisterView.as_view(),name='login')
]
