from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('', include('main.urls', namespace='main')),
    # http://127.0.0.1:8000/users
    path('users/', include('users.urls', namespace='users')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

