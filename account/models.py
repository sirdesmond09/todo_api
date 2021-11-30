from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    

    def __str__(self):
        return self.username


