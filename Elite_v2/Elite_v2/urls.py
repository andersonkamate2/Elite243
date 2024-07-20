from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('elite/', admin.site.urls),
    path('', include('KwetuProduction.urls')),
    path('connexion/', include('accounts.urls')),
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)
