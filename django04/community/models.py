from django.db import models

# Create your models here.

class Category(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.name)

class Article(models.Model):
    category_num = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE,
        related_name='article',
    )
    title = models.CharField(max_length=20)
    writing_time = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return str(self.category_num)
