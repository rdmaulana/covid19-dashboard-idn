from django.db import models

# Create your models here.
class covidRecord(models.Model):
    country = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    active = models.CharField(max_length=255)
    recovered = models.CharField(max_length=255)
    new_cases = models.CharField(max_length=255, blank=True, null=True)
    new_deaths = models.CharField(max_length=255, blank=True, null=True)
    total_deaths = models.CharField(max_length=255, blank=True, null=True)
    total_tests = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    latest_update = models.DateTimeField()

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'covid_record'
        verbose_name_plural = 'MASTER COVID DATA RECORD'



