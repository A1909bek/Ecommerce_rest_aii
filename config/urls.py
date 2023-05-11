
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('roads/', include('roads.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'), name='registration'),
    path('allauth', include('allauth.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

