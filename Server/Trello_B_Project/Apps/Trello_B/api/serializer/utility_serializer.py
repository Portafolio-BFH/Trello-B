from Trello_B_Project.Apps.Trello_B.models import Dashboard
from rest_framework import serializers

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        exclude = ['created_date', 'updated_date', 'deleted_date', 'created_by', 'updated_by','deleted_by',]