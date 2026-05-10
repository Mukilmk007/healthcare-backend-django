from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingViewSet(viewsets.ModelViewSet):

    queryset = PatientDoctorMapping.objects.all()

    serializer_class = MappingSerializer

    permission_classes = [IsAuthenticated]