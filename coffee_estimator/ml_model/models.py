from django.db import models
from .countries import COUNTRIES 
from .variety import COFFEE_VARIETIES
from .company import COFFEE_COMPANIES
from .region import REGION_CHOICES  # Import the list of coffee varieties from your separate file # Import the list of countries from your separate file
  # Import the list of coffee varieties from your separate file # Import the list of countries from your separate file


SPECIES_CHOICES = [
        ('Arabica', 'Arabica'),
        ('Robusta', 'Robusta'),
        # Add more choices here
    ]

PROCESSING_METHODS = [
        ('processing_method', 'Processing Method'),  # This looks like a placeholder, you can replace it with actual choices
        ('Washed', 'Washed / Wet'),
        ('Natural', 'Natural / Dry'),
        ('Semi-washed', 'Semi-washed / Semi-pulped'),
        ('Pulped_natural', 'Pulped natural / honey'),]


class Coffee(models.Model):


    PROCESSING_METHOD_CHOICES = [
        ('processing_method', 'Processing Method'),  # This looks like a placeholder, you can replace it with actual choices
        ('Washed', 'Washed / Wet'),
        ('Natural', 'Natural / Dry'),
        ('Semi-washed', 'Semi-washed / Semi-pulped'),
        ('Pulped_natural', 'Pulped natural / honey'),
        # Add more choices here
    ]

        # Add more choices here

    species = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    variety = models.CharField(max_length=255)
    processing_method = models.CharField(max_length=255)
    altitude_mean_meters = models.FloatField()

    # Other fields and methods for your model
