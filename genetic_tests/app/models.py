from django.db import models
from django.utils.timezone import now

class GeneticTest(models.Model):
    animal_name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    test_date = models.DateField()
    milk_yield = models.FloatField()
    health_status = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    created_at = models.DateTimeField(default=now)
