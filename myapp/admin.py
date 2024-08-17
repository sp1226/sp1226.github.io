from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import Task, Board, ImageResult, Reservation
from sp.models import Employee

#게시판 관리 모델 등록
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_date')
    search_fields = ('title', 'content')

# 이미지 업로드 모델 등록
@admin.register(ImageResult)
class ImageResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'img_path', 'date')
    search_fields = ('user__username', 'img_path')

# 직원 관리 모델 등록
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'workload')
    search_fields = ('name', 'position')

# 청소 서비스 예약 관리 모델 등록
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reserve_date', 'region')
    search_fields = ('user__username', 'region')

# 청소 작업 관리 모델 등록
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'date', 'result')
    search_fields = ('emp_id',)    

# 현재 앱의 모든 모델을 가져옴
models = apps.get_models()

# 모든 모델을 Admin에 등록
for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        # 모델이 이미 등록되어 있으면 건너뜀
        pass
