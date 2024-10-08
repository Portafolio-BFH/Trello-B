from django.db import models
from simple_history.models import HistoricalRecords
from Trello_B_Project.Apps.Base.models import ModelBase

# Create your models here.
class Dashboard(ModelBase):
    id = models.AutoField(verbose_name='Dashboard ID', primary_key=True)
    title = models.CharField(verbose_name='Título',max_length=60, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'Dashboard'
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'

    def __str__(self):
        return self.title
