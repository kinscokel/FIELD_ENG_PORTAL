from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model with role
class User(AbstractUser):
    ROLE_CHOICES = (
        ('engineer', 'Engineer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.model import User

class Post(models.Model):
    tittle=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Post')
    tittle=models.ForeignKey(tittle, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self, User):
        return f "{self.User}.comment on {post} "




    
