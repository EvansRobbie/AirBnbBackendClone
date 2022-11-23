from django.db import models

# Create your models here.
class Apartments(models.Model):
    name = models.CharField(max_length= 255)
    country = models.CharField(max_length= 255)
    city =models.CharField(max_length=255)
    distance = models.DecimalField(max_digits = 10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits= 10 ,decimal_places=2)
    beds = models.IntegerField(default=1)
    lat = models.DecimalField(max_digits = 10, decimal_places = 6)
    long =models.DecimalField(max_digits = 10, decimal_places = 6)
    image = models.ImageField(null=True, blank=True)
    bedrooms =models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    check_in = models.TextField(default="00:00:00")
    check_out =models.TextField(default="00:00:00")
    ratings = models.IntegerField(default = 1)
    instant_book = models.BooleanField(default=False)
    # https://stackoverflow.com/questions/63325929/django-multiple-pictures-one-product

    def __str__(self) :
        return self.name
     # avoid the error if a product doesn't have an image
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

