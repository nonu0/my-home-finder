from django.urls import path
from apps.houses.views import HomeView,PropertyView,AgentView,ContactView,BlogView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('properties',PropertyView.as_view(),name='properties'),
    path('agent',AgentView.as_view(),name='agent'),
    path('contact',ContactView.as_view(),name='contact'),
    path('blog',BlogView.as_view(),name='blog'),
]
