from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_inventory.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
    # По адресу api/schema/ будет генерироваться JSON-схема API, из которой по адресу api/schema/swagger-ui/
    # будет строиться Swagger-UI документация. api/schema/redoc URL предоставляет интерфейс ReDoc для вашей схемы API
]
