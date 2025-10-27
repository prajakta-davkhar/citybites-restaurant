from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    time = models.TimeField(null=True, blank=True)
    people = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"