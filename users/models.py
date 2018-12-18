from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels


# # Create your models here.
# class User(AbstractUser):
#     pass

class Farmer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="farmer")
    name = models.CharField("Legal name", max_length=255)
    phone_number = models.CharField("Contact number", max_length=20)

class FarmMap(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geom = geomodels.PointField()
    slug = models.SlugField(default=None, unique=False)

    class Meta:
        ordering = ('name',)

        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name
    