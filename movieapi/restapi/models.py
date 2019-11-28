from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# objects = models.Manager()

class VehicleMaintenance(models.Model):
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=200, blank=False, null=False)
    location = models.CharField(max_length=200, blank=False, null=False)
    service = models.CharField(max_length=200, blank=False, null=False)
    mileage = models.IntegerField(blank=False, null=False)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    # name = models.CharField(max_length=200, blank=False, null=False)
    # rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    # class Meta:
    #     unique_together = [ ['user', 'name' ] ]

    def __str__(self):
        return f'Vehicle: {self.vehicle}. Maintenance Performed: {self.service}. Mileage: {self.mileage}.' # belongs to {self.user}'