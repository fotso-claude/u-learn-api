# Generated by Django 4.1.2 on 2022-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_alter_training_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='training',
            field=models.ManyToManyField(blank=True, related_name='tags', to='training.training'),
        ),
    ]