from django.db import models

class PoliceReport(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('Thief', 'Thief'),
        ('Fire Accident', 'Fire Accident'),
        ('Crashing', 'Crashing'),
        ('Emergency', 'Emergency'),
    ]

    incident_type = models.CharField(
        max_length=100,
        choices=INCIDENT_TYPE_CHOICES,
        default='None'
    )
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'Report: {self.incident_type} at {self.location}'
