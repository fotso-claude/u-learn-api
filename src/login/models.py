from enum import Enum

from django.db import models


class User(models.Model):
    class Role(Enum):
        ADMIN = 1
        TEACHER = 2
        STUDENT = 3

    user_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.IntegerField(
        max_length=1,
        choices=Role,
        default=Role.STUDENT
    )

    def __str__(self):
        return f"User infos : id: {self.user_id}, name: {self.name}, email: {self.email}, role: {self.role}"
