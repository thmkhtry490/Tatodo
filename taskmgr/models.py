from django.db import models
from django.contrib.auth.models import User
# It's task model is save in database
class Task(models.Model):
    """
    This is a model in database for tasks. 
    Have user, title,text,create_time and done fields. 
    return task title when use in template.
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=800)
    text = models.TextField(blank=True, null=True,max_length=1800)
    create_time = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title