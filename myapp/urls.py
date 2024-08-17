from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import viewsets_dict
from . import views
from rest_framework import routers
from .views import TaskViewSet
from django.contrib.auth.decorators import login_required, user_passes_test

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# 동적으로 모든 뷰셋을 라우터에 등록
for model_name, viewset_class in viewsets_dict.items():
    router.register(model_name.lower(), viewset_class)

urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.home_view, name='home'),
    path('board/', login_required(views.board_view), name='board'),
    path('upload/', user_passes_test(lambda u: u.is_staff)(views.upload_view), name='upload'),
]
