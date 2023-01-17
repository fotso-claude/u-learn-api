from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from training.models import Training, Tag, Category, Chapter


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'training']
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [UniqueValidator(queryset=Tag.objects.all())]
            },
            'training': {'required': False}
        }


class CategorySerializer(serializers.ModelSerializer):
    # training = TrainingSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [UniqueValidator(queryset=Training.objects.all())]
            }
        }


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['title']
        extra_kwargs = {'title': {'required': True, }}


class TrainingSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    # tags = serializers.SerializerMethodField(many=True)

    class Meta:
        model = Training
        fields = ['name', 'description', 'duration', 'price', 'image_url', 'registered', 'status', 'category', 'tags',
                  'chapters', 'file_url']
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [UniqueValidator(queryset=Training.objects.all())],
            },
            'description': {'required': True},
            'price': {'required': True},
            'duration': {'required': True},
            'image_url': {'required': False},
            'category': {'required': True},
            'tags': {'required': False},
            'chapters': {'required': False},
            'file_url': {'required': False},
        }

    def validate_status(self, status):
        if status is not None and status not in ['coming', 'available']:
            raise serializers.ValidationError("status invalid.")
        return status

    def create(self, validated_data):
        training = Training.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            duration=validated_data['duration'],
            category=validated_data['category'],
        )

        if validated_data['image_url'] is not None:
            training.image_url = validated_data['image_url']

        if validated_data['status'] is not None:
            training.status = validated_data['status']

        training.save()
        return training

    # def get_tags(self, instance):
    #     queryset = instance.tags.filter
    #     return TagSerializer(instance.tags, many=True).data
