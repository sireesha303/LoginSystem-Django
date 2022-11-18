from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='profiles/')
    git_url = models.CharField(null=True, blank=True, max_length=100)
    linkedin_url = models.CharField(null=True, blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.username


