from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    path('', include('help.urls')),
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Baba-Help"
admin.site.site_title = "Baba-Help"
admin.site.index_title = "Baba-Help"