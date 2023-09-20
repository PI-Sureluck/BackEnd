from django.urls import path

from .views import SiteView

urlpatterns = [
    path('site/', SiteView.as_view(), name='site_list'),
    path('site/<int:id>', SiteView.as_view(), name='site_process')
]