from django.contrib import admin
from django.urls import path, include
import app0725.views
import app0725.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', app0725.views.home, name="home"),
    path('blog/', include(app0725.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
