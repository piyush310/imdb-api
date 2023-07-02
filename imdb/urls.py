from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework.decorators import api_view
# from django.urls import re_path
from django.urls import path, include
from django.contrib import admin
from django.http import JsonResponse
from rest_framework import status
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(title="Snippets API", default_version='v1'),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)


def health_check(request):
    return JsonResponse({
        "status": status.HTTP_200_OK,
        "message": "health check"
    })


urlpatterns = [
    path("", health_check, name="healthcheck"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('watch/api/v1/', include('watchlist.urls')),
    path('swagger<format>/',
         schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('docs/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc')
]
