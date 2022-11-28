from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from training.models import Training, Tag, Category


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['name', 'description', 'duration', 'image_url', 'registered', 'status']
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [UniqueValidator(queryset=Training.objects.all())],
            },
            'description': {'required': True},
            'duration': {'required': True},
            'category': {'required': True}
        }

    def create(self, validated_data):
        training = Training.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            duration=validated_data['duration'],
            image_url=validated_data['image_url'],
            status=validated_data['status'],
        )
        training.save()
        category = Category.objects.get(pk=validated_data["category"])
        category.add(training)
        return training


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {'required': True}
        }


class CategorySerializer(serializers.ModelSerializer):

    #training = TrainingSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [UniqueValidator(queryset=Training.objects.all())]
            }
        }
