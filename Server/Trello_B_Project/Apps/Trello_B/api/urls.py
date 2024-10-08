from django.urls import path
from Trello_B_Project.Apps.Trello_B.api.views.dashboard_view import *
from Trello_B_Project.Apps.Trello_B.api.views import *

urlpatterns = [
    path('dashboard/', DashboardListAPIView.as_view(), name='Dashboard List'),
    path('dashboard/<int:pk>/', DashboardRetrieveAPIView.as_view(), name='Dashboard By Id'),
    path('dashboard/create/', DashboardCreateAPIView.as_view(), name='Dashboard Create'),
    path('dashboard/delete/<int:pk>/', DashboardDestroyAPIView.as_view(), name='Dashboard Delete'),
 ]