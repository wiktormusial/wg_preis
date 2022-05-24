from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city

    def __save__(self):
        if not self.slug:
            self.slug = slugify(self.city)
        return super().save(*args, **kwargs)


class Price(models.Model):
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)