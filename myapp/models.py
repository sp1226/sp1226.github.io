# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Task(models.Model):
    task_id = models.BigIntegerField(primary_key=True)
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING)
    date = models.DateTimeField()
    emp_id = models.IntegerField()
    result = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Task'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Board(models.Model):
    board_id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board'


class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=255)
    create_at = models.DateTimeField(blank=True, null=True)
    board = models.ForeignKey(Board, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emp(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=50)
    region = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    workload = models.IntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'emp'


class ImageResult(models.Model):
    image_id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_result'


class ImageResultSeq(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_result_seq'


class Reservation(models.Model):
    reservation_id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField()
    region = models.CharField(max_length=255)
    reserve_date = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reservation'


class SolarPanels(models.Model):
    solar_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    panel_area = models.FloatField()
    installation_date = models.DateField()
    region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'solar_panels'


class SpProduct(models.Model):
     id = models.BigAutoField(primary_key=True)
     name = models.CharField(max_length=100)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     created_at = models.DateTimeField()

     class Meta:
         managed = False
         db_table = 'sp_product'


class SpSolarpanel(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    panel_area = models.FloatField()
    installation_date = models.DateField()
    region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sp_solarpanel'


class Tasks(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    emp_id = models.BigIntegerField()
    result = models.CharField(max_length=255, blank=True, null=True)
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tasks'


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
