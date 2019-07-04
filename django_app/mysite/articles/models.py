from django.db import models
from django.utils import timezone
# Create your models here.
class Site(models.Model):
    site_name = models.CharField(max_length=200)
    def __str__(self):
        return self.site_name

class Article(models.Model):
    text = models.CharField(max_length=200)
    title = models.CharField(max_length=20000)
    pub_date = models.DateTimeField('date published')
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
