from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  head_image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True)
  dt_create = models.DateTimeField(auto_now_add=True)
  dt_update = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return f'/post/{self.pk}/'
  