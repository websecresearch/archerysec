# Generated by Django 2.1.8 on 2020-05-15 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0008_dockle_scan_db_dockle_scan_results_db'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dockle_scan_db',
            old_name='inspec_info',
            new_name='dockle_info',
        ),
        migrations.RenameField(
            model_name='dockle_scan_db',
            old_name='inspec_pass',
            new_name='dockle_pass',
        ),
    ]