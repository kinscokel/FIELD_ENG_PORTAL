


from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer
from .permissions import IsAdminOrReadOnly, IsTaskOwnerOrAdmin

# ---------------------------
# ViewSets (DRF)
# ---------------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsAdminOrReadOnly()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsTaskOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# Simple function-based view


# Home route view
def home_view(request):
    return HttpResponse("Welcome to the Field Engineer Portal API")

# API root fallback (optional)
def api_root(request):
    return HttpResponse("Welcome to the API root!")

# Test view
def post_detail(request, post_id):
    return HttpResponse(f"Post ID is {post_id}")

# Real task JSON view
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")

    data = {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "assigned_to": task.assigned_to.username,
        "created_by": task.created_by.username,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
    }
    return JsonResponse(data)