from django.db import models

class Outsourcing(models.Model):
    ossn = models.CharField(max_length=50, null=True, blank=True)
    osqu = models.CharField(max_length=50, null=True, blank=True)
    osdate = models.DateTimeField()

    def __str__(self):
        return self.ossn

class Manufacture(models.Model):
    proname = models.CharField(max_length=50, null=True, blank=True)
    mfsn = models.CharField(max_length=50, null=True, blank=True)
    origin = models.CharField(max_length=50, null=True, blank=True)
    halfpro = models.CharField(max_length=50, null=True, blank=True)
    workercode = models.CharField(max_length=50, null=True, blank=True)
    mfsta = models.CharField(max_length=50, null=True, blank=True)
    mfdate = models.DateTimeField()

    def __str__(self):
        return self.proname

class Logistics(models.Model):
    logname = models.CharField(max_length=50, null=True, blank=True)
    logsn = models.CharField(max_length=50, null=True, blank=True)
    wh = models.CharField(max_length=50, null=True, blank=True)
    dis = models.CharField(max_length=50, null=True, blank=True)
    agen = models.CharField(max_length=50, null=True, blank=True)
    logcustom = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.logname

class As(models.Model):
    asname = models.CharField(max_length=50)
    ph = models.CharField(max_length=50)
    pronumber = models.CharField(max_length=50)
    assta = models.CharField(max_length=50, null=True, blank=True)
    record = models.FileField(null=True, blank=True)
    asdate = models.DateTimeField()

    def __str__(self):
        return self.asname