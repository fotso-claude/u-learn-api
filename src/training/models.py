from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Training(models.Model):
    class Status(models.TextChoices):
        COMING = "coming"
        AVAILABLE = "available"

    name = models.CharField(max_length=255)
    description = models.TextField()
    registered = models.IntegerField(default=0)
    status = models.CharField(
        max_length=9,
        choices=Status.choices,
        default=Status.COMING
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    training = models.ManyToManyField(Training)
