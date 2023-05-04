from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskView

urlpatterns = [
    path('auth-token/', obtain_auth_token, name="api_auth_token"),
    path('tasks/', TaskView.as_view(), name="list_tasks"),
    path('tasks/<int:id>/', TaskView.as_view(), name="list_tasks"),
]