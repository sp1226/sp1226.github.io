from rest_framework import viewsets
from .models import *
from .serializers import serializers_dict
import inspect
from django.db import models as django_models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .serializers import TaskSerializer

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def upload_view(request):
    return render(request, 'upload.html')

@login_required
def board_view(request):
    return render(request, 'board.html')

def home_view(request):
    return render(request, 'home.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# 동적으로 모든 모델에 대한 뷰셋 생성
viewsets_dict = {}

for model in models.__all__:
    model_class = getattr(models, model)

    # model_class가 클래스이고, Django 모델이지만 Model 클래스 자체가 아닌지 확인
    if inspect.isclass(model_class) and issubclass(model_class, django_models.Model) and model_class is not django_models.Model:
        serializer_class = serializers_dict[model]
        viewset_class = type(f'{model}ViewSet', (viewsets.ModelViewSet,), {
            'queryset': model_class.objects.all(),
            'serializer_class': serializer_class
        })
        globals()[f'{model}ViewSet'] = viewset_class
        viewsets_dict[model] = viewset_class

# 로그인 여부 확인
@login_required
def some_view(request):
    # 여기에 게시판 기능 등의 로직을 작성합니다.
    pass

# 관리자인지 확인
def is_admin(user):
    return user.is_superuser  # 슈퍼유저(관리자)만 접근 가능

@user_passes_test(is_admin)
def another_view(request):
    # 여기에 직원 관리 등의 로직을 작성합니다.
    pass


# 특정 권한이 있는지 확인
@permission_required('app_name.permission_codename')
def some_protected_view(request):
    # 여기에 권한이 필요한 로직을 작성합니다.
    pass