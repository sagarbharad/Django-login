from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    unique = models.CharField( max_length=50, default='')
    email = models.EmailField()
    password = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='uploads/', default="", null=True)
    def __str__(self):
        return str(self.first_name)

    @staticmethod
    def get_user_by_email(email):
        try:
            return Client.objects.get(email=email)
        except:
            return False

