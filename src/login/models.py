from django.contrib.auth.models import User
from django.db import models


class Auth(User):
    role = models.CharField(
        max_length=7,
        default="student"
    )

    training = models.ManyToManyField('training.Training', related_name="training", blank=True)

    def __str__(self):
        return self.username
