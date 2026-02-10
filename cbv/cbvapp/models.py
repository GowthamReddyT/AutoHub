from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='logo/',blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    cc = models.IntegerField()
    Mileage = models.DecimalField(max_digits=5, decimal_places=2)
    pro_img = models.ImageField(upload_to='prodimg/',blank=True,null=True)


    def __str__(self):
        return self.product_name


class Interior(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="interiors",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/interior/")

    def __str__(self):
        return f"{self.product.Product_Name} Interior"


# ✅ NEW MODEL – Exterior
class Exterior(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="exteriors",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/exterior/")

    def __str__(self):
        return f"{self.product.Product_Name} Exterior"