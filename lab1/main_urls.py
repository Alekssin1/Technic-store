from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


urlpatterns += [
    path('admin', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('users_page.urls')),
    path('catalog/', include('catalog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
