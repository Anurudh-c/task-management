from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define schema view for Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Task Management API",  
      default_version='v1',  
      description="This API allows you to manage tasks including creating, viewing, editing, and deleting tasks.",
   ),
   public=True,  
   permission_classes=(permissions.AllowAny,),  
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
