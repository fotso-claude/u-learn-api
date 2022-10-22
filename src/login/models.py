from django.db import models


class User(models.Model):
    class Role(models.IntegerChoices):
        ADMIN = 1
        TEACHER = 2
        STUDENT = 3

    name = models.CharField(max_length=200)
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    password = models.CharField(max_length=255)
    role = models.IntegerField(
        choices=Role.choices,
        default=Role.STUDENT
    )

    def __str__(self):
        return f"User infos -- name: {self.name}, email: {self.email}, role: {self.role}"
