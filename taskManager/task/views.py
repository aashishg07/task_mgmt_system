from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class TaskView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = IsAuthenticated,
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    
    def get(self, request, id=None, employee=None, format=None):
        task_model = Task
        if request.user.is_superuser:

            if employee:
                tasks = task_model.objects.filter(created_by=User)
            elif id:
                tasks = task_model.objects.filter(id=id)
            else:
                tasks = task_model.objects.all()
        else:
 
            if id:
                tasks = task_model.objects.filter(id=id, created_by=User)
            else:
                tasks = task_model.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.created_by = request.user
            task.save()
            response_dict = serializer.data
            response_dict['created_by'] = request.user.username # add task created employee's name
            return Response(response_dict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)