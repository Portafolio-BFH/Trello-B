from rest_framework import generics
from Trello_B_Project.Apps.Base.api import *
from Trello_B_Project.Apps.Trello_B.api.serializer.utility_serializer import *

class DashboardListAPIView(GeneralListAPIView):
    serializer_class = DashboardSerializer

class DashboardRetrieveAPIView(GeneralRetrieveAPIView):
    serializer_class = DashboardSerializer

class DashboardCreateAPIView(GeneralCreateAPIView):
    serializer_class = DashboardSerializer
    message_success = "Dashboard created successfully"

class DashboardDestroyAPIView(GeneralDestroyAPIView):
    serializer_class = DashboardSerializer
    message_success = "Dashboard deleted successfully"
    message_notfound = "Dashboard not found"