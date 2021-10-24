from django.db import models

# Create your models here.
class experience(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    summary = models.TextField(max_length=300, null=True, blank=True)
    url = models.CharField(max_length=40, null=True)
    duree = models.CharField(max_length=50)
    Type = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name