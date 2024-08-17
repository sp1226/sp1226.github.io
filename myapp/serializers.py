from rest_framework import serializers
from .models import *
from django.apps import apps
from .models import Task

# 모든 모델 가져오기
#models = apps.get_models()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# 동적으로 모든 모델에 대한 시리얼라이저 생성
serializers_dict = {}

for model in models.__all__:
    model_class = getattr(models, model)
    serializer_class = type(f'{model}Serializer', (serializers.ModelSerializer,), {
        'Meta': type('Meta', (), {
            'model': model_class,
            'fields': '__all__'
        })
    })
    globals()[f'{model}Serializer'] = serializer_class
    serializers_dict[model] = serializer_class

    