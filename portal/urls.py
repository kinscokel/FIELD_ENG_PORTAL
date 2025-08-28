"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('enghub.urls')),
]


from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('api/')),  # Redirect root to /api/
    path('admin/', admin.site.urls),
    path('api/', include('enghub.urls')),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enghub.views import (
    TaskViewSet, UserViewSet, post_detail, home_view, task_detail
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ✅ Handles all /api/tasks and /api/users
    path('api/post/<int:post_id>/', post_detail, name='post_detail'),  # ✅ Test path
    path('api/task/<int:task_id>/', task_detail, name='task_detail'),  # ✅ JSON Task view
]
