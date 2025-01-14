from django.shortcuts import render
from rest_framework import viewsets 
from movieapi.restapi.serializers import VehicleMaintenanceSerializer
from movieapi.restapi.models import VehicleMaintenance
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Hello Android Students.')


class VehicleMaintenanceViewSet(viewsets.ModelViewSet):

    serializer_class = VehicleMaintenanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return VehicleMaintenance.objects.filter(user=self.request.user).order_by('date')

    def create(self, request):
        try:
            print("creating", request.data)
            vehicle = VehicleMaintenance(date=request.data['date'], service=request.data['service'], user=request.user, mileage=request.data['mileage'], 
            notes=request.data['notes'], vehicle=request.data['vehicle'], location=request.data['location']).save()
            return Response(vehicle, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
