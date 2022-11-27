from django.contrib.auth.models import User
from django.db import models

from training.models import Training


class Auth(User):
    role = models.CharField(
        max_length=7,
        default="student"
    )

    training = models.ManyToManyField(Training)

    def __str__(self):
        return self.username
