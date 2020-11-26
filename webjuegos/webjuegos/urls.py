from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls')),
    path('accounts/',include('sesion.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),name='home')
]

urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)