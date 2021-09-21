
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Sodai Admin"
admin.site.site_title = "Sodai"
admin.site.index_title = "Sodai Administration Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
