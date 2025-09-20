from django.db import models

class Smart_Phones(models.Model):
    model = models.CharField(null=False,max_length=50)
    brand = models.CharField(null=False,max_length=50)
    image = models.ImageField(null=False)
    Processor = models.CharField(null=False,max_length=50)
    display = models.CharField(null=False,max_length=50)
    ram = models.CharField(null=False,max_length=50,default=8)
    storage = models.CharField(null=False,max_length=50)
    colours = models.CharField(null=False,max_length=50)
    batteryCapacity = models.CharField(null=False,max_length=50)
    resolution = models.CharField(null=False,max_length=50)
    rearCamera = models.CharField(null=False,max_length=50)
    frontCamera = models.CharField(null=False,max_length=50)
    amazon = models.CharField(null=False,max_length=50)
    flipkart = models.CharField(null=False,max_length=50)
    Reliance = models.CharField(null=False,max_length=50)
    Brand_site = models.CharField(null=False,max_length=50)

    def __str__(self):
        return f"{self.brand} - {self.model}"

class Laptops(models.Model):
    model = models.CharField(null=False,max_length=50)
    brand = models.CharField(null=False,max_length=50)
    image = models.ImageField(null=False)
    Processor = models.CharField(null=False,max_length=50)
    display = models.CharField(null=False,max_length=50)
    graphics = models.CharField(null=False,max_length=50)
    ram = models.CharField(null=False,max_length=50,default=8)
    Memory_Storage = models.CharField(null=False,max_length=50)
    Resolution = models.CharField(null=False,max_length=50)
    batteryCapacity = models.CharField(null=False,max_length=50)
    Features = models.CharField(null=False,max_length=100)
    amazon = models.CharField(null=False,max_length=50)
    flipkart = models.CharField(null=False,max_length=50)
    Reliance = models.CharField(null=False,max_length=50)
    Brand_site = models.CharField(null=False,max_length=50)

    def __str__(self):
        return f"{self.brand} - {self.model}"
    
class Smart_Watches(models.Model):
    model = models.CharField(null=False,max_length=50)
    brand = models.CharField(null=False,max_length=50)
    image = models.ImageField(null=False)
    Processor = models.CharField(null=False,max_length=50)
    display = models.CharField(null=False,max_length=50)
    Weight = models.CharField(null=False,max_length=50)
    Colors = models.CharField(null=False,max_length=50)
    Sensors = models.CharField(null=False,max_length=100)
    Resolution = models.CharField(null=False,max_length=50)
    batteryCapacity = models.CharField(null=False,max_length=50)
    Features = models.CharField(null=False,max_length=100)
    amazon = models.CharField(null=False,max_length=50)
    flipkart = models.CharField(null=False,max_length=50)
    Reliance = models.CharField(null=False,max_length=50)
    Brand_site = models.CharField(null=False,max_length=50)

    def __str__(self):
        return f"{self.brand} - {self.model}"

# Create your models here.
