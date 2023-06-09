from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('app_1:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}' . format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='products')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('app_1:prodCatdetails', args=[self.category.slug, self.slug])
    class Meta:
        ordering = ('name', )
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}' . format(self.name)

