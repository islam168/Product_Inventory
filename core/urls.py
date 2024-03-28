from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_inventory.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
    # The api/schema/ URL will generate the JSON API schema, from which the api/schema/swagger-ui
    # URL will build the Swagger-UI documentation. api/schema/redoc URL provides
    # the ReDoc interface for your API schema
]
