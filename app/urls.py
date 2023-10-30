from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]

# serve media files in development environment --------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# debug toolbar ---------------------------------------------------------------
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# admin site customizations ---------------------------------------------------
admin.sites.AdminSite.site_header = f"{settings.APP_NAME} Administration"
admin.sites.AdminSite.site_title = f"{settings.APP_NAME} Administration"
admin.sites.AdminSite.index_title = f"{settings.APP_NAME} Admin Panel"
