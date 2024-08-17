from rest_framework import serializers
from .models import *

# 데이터베이스의 모든 테이블에 대해 시리얼라이저 생성
class DynamicSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 동적으로 설정
        fields = '__all__'

def generate_serializers():
    serializers_dict = {}
    for model in models.__all__:
        Meta = type('Meta', (), {'model': getattr(models, model), 'fields': '__all__'})
        serializer_class = type(f'{model}Serializer', (DynamicSerializer,), {'Meta': Meta})
        serializers_dict[model] = serializer_class
    return serializers_dict

serializers = generate_serializers()