from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from . import views

urlpatterns = [
    # Your other routes
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]