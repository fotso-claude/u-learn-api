from django.contrib.auth.models import User
from django.db import models


class Auth(User):
    role = models.CharField(
        max_length=7,
        default="student"
    )
