from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

# Note: remember to 'python manage.py makemigrations car_list' and 'python manage.py migrate' to create table
# Also add 'car_list' app to setting INSTALLED_APPS
# This will generate migration files in the migrations directory of the 'car_list' app
# 'migrate' command to apply the changes to the database

# To add a new car to the database, first navigate to 'my_website' directory
# Then 'py manage.py shell' ; 'from car_list.models import Car'
# Then example: car1 = Car(make='Toyota', model='Camry', year=2022, color='Blue')
# Then 'car1.save()'
# Check to see if the records are saved in db: 'Car.objects.all()'