# Generated by Django 3.1.12 on 2021-07-19 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20210719_1431'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdb',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projectdb',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='monthdb',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectdb'),
        ),
    ]
