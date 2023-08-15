from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task_app.views import ProjectModelViewSet, TaskModelViewSet
from rest_framework import permissions
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo Application",
        default_version='v1',
        description="Test Swagger First app",
        terms_of_service="http://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@todo.local"),
        license=openapi.License(name="Test License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'projects', ProjectModelViewSet)
router.register(r'tasks', TaskModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swag/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
