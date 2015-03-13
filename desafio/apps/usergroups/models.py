from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


class UserGroup(Group):
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name