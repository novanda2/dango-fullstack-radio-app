from django.urls.conf import path
from dango.apps.podcast import views


urlpatterns = [
    path("", views.test_lang)
]
