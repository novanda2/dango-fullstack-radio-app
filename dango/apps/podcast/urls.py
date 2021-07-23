from django.conf.urls.i18n import i18n_patterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PodcastListView.as_view()),
    path('<int:pk>/', views.PodcastDetailView.as_view()),
    path('test/', views.test_lang)
]

# urlpatterns += i18n_patterns(
#     path('', views.PodcastListView.as_view(), name='index'),
#     path('<int:pk>/', views.PodcastDetailView.as_view(), name='detail'),
#     path('test/', views.test_lang)
# )