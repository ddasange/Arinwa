
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns






urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('arinwa/', include('essai1.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)