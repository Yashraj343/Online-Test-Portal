from django.db import models

class Login(models.Model):
    email = models.EmailField(primary_key=True)
    password= models.CharField(max_length=100)
    admin=models.BooleanField(default=False)
    test_taken = models.BooleanField(default=False)
    def __str__(self):
        return self.email

