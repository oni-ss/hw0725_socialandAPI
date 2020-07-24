from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='app0725/defaultimage/aaa.jpg')
    pub_date = models.DateTimeField('daet published')
    body = models.TextField()

    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(360,360)])

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:60]