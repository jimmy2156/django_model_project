from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Countries"





class Address(models.Model):
    street_number = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    street_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.street_name}, {self.street_name} {self.country} {self.postal_code}"
    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()






class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, null=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("single_book", args=[self.slug])
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
