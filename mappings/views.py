from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingViewSet(viewsets.ModelViewSet):

    queryset = PatientDoctorMapping.objects.all()

    serializer_class = MappingSerializer

    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_doctors_by_patient(self, request, patient_id=None):

        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id
        )

        serializer = self.get_serializer(mappings, many=True)

        return Response(serializer.data)