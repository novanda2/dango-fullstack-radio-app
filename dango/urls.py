from django.urls.conf import include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = i18n_patterns(
    re_path(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    re_path(r'^', include(('dango.apps.podcast.urls', 'podcast'), namespace="podcast"), name="podcast"),
    re_path("admin/", admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
