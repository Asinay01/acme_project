from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = 'core.views.page_not_found'
urlpatterns = [
    path('', include('pages.urls')),
    path('auth/registration/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
