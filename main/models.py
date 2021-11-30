from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_do', null=True,blank=True)
    activity = models.CharField(max_length=350)
    completed =  models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.activity} for {self.user.username}'
    
    
    def delete(self):
        self.is_active = False
        self.save()
        return
    
    