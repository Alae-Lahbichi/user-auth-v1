from django.db import models

# Create your models here.


class product (models.Model):
     
    STATUS_CHOICES = [
        ('available', 'Available ✅'),
        ('unavailable', 'Unavailable ❌'),
    ]
    title = models.CharField(max_length=50 , blank=False )
    status = models.CharField(max_length=12,
        choices=STATUS_CHOICES,
        default='available',
    )
    description = models.TextField(
        max_length=200 , 
        blank=False
    )
    file = models.ImageField(upload_to='images/' , default='madia/default-product.jpg')

    def __str__(self):
        return self.title
