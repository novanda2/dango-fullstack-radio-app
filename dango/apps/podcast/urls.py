from django.urls import path

from . import views

urlpatterns = [
    path('', views.PodcastListView.as_view(), name='index'),
    path('<int:pk>/', views.PodcastDetailView.as_view(), name='detail')
]
