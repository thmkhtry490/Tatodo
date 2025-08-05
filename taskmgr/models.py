from django.db import models
from django.contrib.auth.models import User
# It's task model is save in database
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=800)
    text = models.TextField(blank=True, null=True,max_length=1800)
    create_time = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title