from django.urls import path

from .views import SiteView, EventView, OddsView

urlpatterns = [
    path('site/', SiteView.as_view(), name='site_list'),
    path('site/<int:id>', SiteView.as_view(), name='site_process'),

    path('event/', EventView.as_view(), name='event_list'),
    path('event/<int:id>', EventView.as_view(), name='event_process'),

    path('odds/', OddsView.as_view(), name='odds_list'),
    path('odds/<int:id>', OddsView.as_view(), name='odds_process'),
]