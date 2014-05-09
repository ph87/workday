from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey,\
        GenericRelation
from django.contrib.auth.models import User


class ReportType(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

class Report(models.Model):
    user = models.ForeignKey(User)
    report_type = models.ForeignKey(ReportType)
    done = models.TextField()
    todo = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

class Attachment(models.Model):
    report = models.ManyToManyField(Report)
    attachment = models.FileField(upload_to='attachment')
    dt_created = models.DateTimeField(auto_now_add=True)
