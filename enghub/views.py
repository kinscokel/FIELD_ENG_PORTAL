from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer
from .permissions import IsAdminOrReadOnly, IsTaskOwnerOrAdmin

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


from django.http import HttpResponse

def post_detail(request, post_id):
    return HttpResponse(f"Post ID is {post_id}")


from django.http import HttpResponse

def api_root(request):
    return HttpResponse("Welcome to the API root!")


from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Field Engineer Portal API")