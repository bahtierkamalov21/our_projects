from .models import Project
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class ProjectViewSet(generics.ListAPIView):
    """
     API endpoint that allows users to be viewed or edited.
     """
    queryset = Project.objects.all().order_by('-data')
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)
