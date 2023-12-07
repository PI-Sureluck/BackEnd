from django.urls import path

from .views import Register, LoginView, UserView, LogoutView

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('register/<int:id>', Register.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('User', UserView.as_view(), name='user'),
    path('logout', LogoutView.as_view(), name='logout')

]