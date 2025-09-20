from django.db import models

class UserRegistration(models.Model):
    firstName = models.CharField(max_length=20 , null=False)
    lastName = models.CharField(max_length=20 , null=False)
    email = models.EmailField(null=False)
    number = models.CharField(max_length=20,null=False)
    feedback = models.CharField(max_length=300, null=False , blank=False)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return f" {self.firstName} - {self.lastName} - {self.email}"
    


# Create your models here.
