from movieapi.restapi.models import VehicleMaintenance 
from rest_framework import serializers 

class VehicleMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMaintenance 
        fields = ['id', 'name', 'rating']

    