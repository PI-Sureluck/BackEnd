from django.urls import path

from .views import UserView

urlpatterns = [
    path('user/', UserView.as_view(), name='user_list'),
    path('user/<int:id>', UserView.as_view(), name='user_process')
]