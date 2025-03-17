from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Milk Tea'),
        ('BL', 'Black Tea'),
        ('GT', 'Green Tea'),
        ('HT', 'Herbal Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_add = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='ML')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
