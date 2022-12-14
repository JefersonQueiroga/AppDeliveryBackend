from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger App Delivery",
        default_version='v1',
        description="Api do sistema delivery",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="jefersonqueiroga@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lojas/', include('pedido.api.urls')),
    path('api/user/',include('usuario.api.urls')),
    path('api/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
