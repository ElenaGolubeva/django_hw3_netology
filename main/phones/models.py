from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return f'{self.name}, {self.price}, {self.release_date}, {self.lte_exist}, {self.slug}'
    
