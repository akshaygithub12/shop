from django.db import models

# Create your models here.


class Menu1(models.Model):
    header = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to='b1/images', default="")
    header1 = models.CharField(max_length=50)
    img2 = models.ImageField(upload_to='b1/images', default="")
    img3 = models.ImageField(upload_to='b1/images', default="")
    header3 = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.header