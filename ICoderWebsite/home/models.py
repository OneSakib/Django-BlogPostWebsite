from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, default='')
    email = models.CharField(max_length=500, default='')
    phone = models.IntegerField(default='')
    content = models.CharField(max_length=50000, default="Not Any Query")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Message from " + self.name + '/' + self.email
