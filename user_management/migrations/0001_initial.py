# Generated by Django 3.1.12 on 2021-07-19 14:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('token_time', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('uu_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'User Roles',
                'db_table': 'user_roles',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('uu_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('pass_token', models.CharField(max_length=255, null=True)),
                ('token_time', models.DateTimeField(auto_now=True, null=True)),
                ('password_updt_time', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.organization')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.userroles')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'User Profiles',
                'db_table': 'user_profile',
            },
        ),
    ]
