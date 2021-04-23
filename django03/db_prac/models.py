from django.db import models

# Create your models here.

class MyClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    student_num = models.IntegerField()

    def __str__(self):
        return str(self.class_num)

class MyStudent(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30)
    intro_text = models.TextField()


