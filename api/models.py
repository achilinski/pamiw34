from django.db import models


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('educational', 'Educational'),
        ('thriller', 'Thriller'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="None")
    date_of_publishing = models.DateField(auto_now_add=False, blank=True, null=True)
    rating = models.FloatField(default=0)


    def __str__(self):
        return self.title
