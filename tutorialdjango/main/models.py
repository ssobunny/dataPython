from django.db import models

class Cafe(models.Model):
  name = models.CharField(max_length = 50)
  mainphoto = models.ImageField(blank=True, null=True)
  content = models.TextField()

  def __str__(self):
    return self.name