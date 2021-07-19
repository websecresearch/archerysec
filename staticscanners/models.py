# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from __future__ import unicode_literals

from django.db import models
from user_management.models import UserProfile

# Create your models here.


class StaticScansDb(models.Model):
    class Meta:
        db_table = "staticscansdb"
        verbose_name_plural = "Static Scans Db"
    project_name = models.TextField(blank=True, null=True)
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    scan_date = models.TextField(blank=True)
    scan_status = models.TextField(blank=True)
    project = models.ForeignKey('projects.ProjectDb', on_delete=models.CASCADE, null=True)
    total_vul = models.IntegerField(blank=True, null=True)
    critical_vul = models.IntegerField(blank=True, null=True)
    high_vul = models.IntegerField(blank=True, null=True)
    medium_vul = models.IntegerField(blank=True, null=True)
    low_vul = models.IntegerField(blank=True, null=True)
    info_vul = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    rescan = models.TextField(blank=True, null=True)
    total_dup = models.TextField(blank=True, null=True)
    scanner = models.CharField(max_length=256, null=True)
    updated_time = models.DateTimeField(auto_now=True, blank=True, null=True)


class StaticScanResultsDb(models.Model):
    class Meta:
        db_table = "staticscanresultsdb"
        verbose_name_plural = "Static Scans Data"
    scan_id = models.UUIDField(blank=True)
    rescan_id = models.TextField(blank=True, null=True)
    project = models.ForeignKey('projects.ProjectDb', on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    vuln_id = models.UUIDField(blank=True)
    false_positive = models.TextField(null=True, blank=True)
    severity_color = models.TextField(blank=True)
    dup_hash = models.TextField(null=True, blank=True)
    vuln_duplicate = models.TextField(null=True, blank=True)
    false_positive_hash = models.TextField(null=True, blank=True)
    vuln_status = models.TextField(null=True, blank=True)
    jira_ticket = models.TextField(null=True, blank=True)
    title = models.TextField(blank=True, null=True)
    severity = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    fileName = models.TextField(blank=True, null=True)
    filePath = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True)
    scanner = models.TextField(blank=True)
    updated_time = models.DateTimeField(auto_now=True, blank=True, null=True)