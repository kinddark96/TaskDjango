from django.db import models

# Create your models here.
class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    courseName=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) +' - '+self.courseName