from django.db import models


def upload_to(instance, filename):
    return f"training/training_{instance.id}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Training(models.Model):
    class Status(models.TextChoices):
        COMING = "coming"
        AVAILABLE = "available"

    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    image_url = models.ImageField(upload_to=upload_to, blank=True, default="training/default.png")
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
    training = models.ManyToManyField('Training', related_name="tags", blank=True)

    def __str__(self):
        return self.name
