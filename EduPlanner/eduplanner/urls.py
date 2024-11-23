"""
URL configuration for eduplanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDetailView, EventDeleteView
)

urlpatterns = [
    path('events/', EventListView.as_view(), name='events_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('admin/', admin.site.urls),
]
