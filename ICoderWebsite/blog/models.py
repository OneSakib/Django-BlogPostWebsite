from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    content = models.TextField(max_length=50000, default="Not Any Query")
    author = models.CharField(max_length=500, default='')
    slug = models.CharField(max_length=600, default='')
    views=models.IntegerField(default=0)
    timestamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to="blogpost/images", default="")

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.user.username
