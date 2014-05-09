from django.db import models
from django.contrib.auth.models import User

class Title(models.Model):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Level(models.Model):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Staff(User):
    title = models.ManyToManyField(Title, related_name='stuff')
    level = models.ForeignKey(Level, null=True)
    superior = models.ManyToManyField('self', symmetrical=False,
            related_name='subordinates')

    def __unicode__(self):
        return '%s %s' % (self.username, self.level or '')

    def get_all_subordinates(self):
        subordinates = {}
        def get_subordinates(staff):
            for subordinate in staff.subordinates.all():
                pre_subs = subordinates
                subordinates[subordinate] = True
                if subordinate.subordinates.all():
                    get_subordinates(subordinate)
                else:
                    pass
        get_subordinates(self)
        return subordinates.keys()
