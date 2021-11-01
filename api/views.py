from rest_framework import viewsets
from .permissions import CustomPermission
from .models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
