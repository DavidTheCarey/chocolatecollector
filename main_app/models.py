from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
chocolates = [
  {'name': 'Melt-Aways', 'type': 'Whipped', 'description': 'A delectable confectionery piece so smooth and so perfect it melts in your mouth', 'flavor': "Milk Chocolate"},
  {'name': 'Butter Cream', 'type': 'Cream Filled', 'description': 'A delicious confectionery piece with a familiar creamy center', 'flavor': "Dark Chocolate"},
]

class Chocolate(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    flavor = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'chocolate_id': self.id})


class Order(models.Model):
  date = models.DateField('Order Date')
  location = models.CharField(
    max_length=100,
    default="Boston"
  )
  # Create a cat_id FK
  chocolate = models.ForeignKey(
    Chocolate,
    on_delete=models.CASCADE
  )

#   def __str__(self):
#     return f"{self.get_location_display()} on {self.date}"

  class Meta:
    ordering = ['-date']