from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey,\
        GenericRelation

from staff.models import Staff


class ReportType(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.code


class Report(models.Model):
    staff = models.ForeignKey(Staff)
    report_type = models.ForeignKey(ReportType)
    done_content = models.TextField()
    todo_content = models.TextField()
    additional = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s %s' % (self.user, self.dt_updated or self.created)


class Attachment(models.Model):
    report = models.ForeignKey(Report, related_name='attachment')
    attachment = models.FileField(upload_to='attachment')
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
