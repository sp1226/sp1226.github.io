from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, AuthGroupViewSet, AuthGroupPermissionsViewSet, AuthPermissionViewSet, AuthUserViewSet, AuthUserGroupsViewSet, AuthUserUserPermissionsViewSet, BoardViewSet, CommentsViewSet, DjangoAdminLogViewSet, DjangoContentTypeViewSet, DjangoMigrationsViewSet, DjangoSessionViewSet, EmpViewSet, ImageResultViewSet, ImageResultSeqViewSet, ReservationViewSet, SolarPanelsViewSet, SpProductViewSet, SpSolarpanelViewSet, TasksViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'authgroup', AuthGroupViewSet)
router.register(r'authgrouppermissions', AuthGroupPermissionsViewSet)
router.register(r'authpermission', AuthPermissionViewSet)
router.register(r'authuser', AuthUserViewSet)
router.register(r'authusergroups', AuthUserGroupsViewSet)
router.register(r'authuseruserpermissions', AuthUserUserPermissionsViewSet)
router.register(r'board', BoardViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'djangoadminlog', DjangoAdminLogViewSet)
router.register(r'djangocontenttype', DjangoContentTypeViewSet)
router.register(r'djangomigrations', DjangoMigrationsViewSet)
router.register(r'djangosession', DjangoSessionViewSet)
router.register(r'emp', EmpViewSet)
router.register(r'imageresult', ImageResultViewSet)
router.register(r'imageresultseq', ImageResultSeqViewSet)
router.register(r'reservation', ReservationViewSet)
router.register(r'solarpanels', SolarPanelsViewSet)
router.register(r'spproduct', SpProductViewSet)
router.register(r'spsolarpanel', SpSolarpanelViewSet)
router.register(r'user', UserViewSet)
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
