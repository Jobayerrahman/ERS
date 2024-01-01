from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    time = models.TimeField() 
    date = models.DateField()
    location = models.CharField(max_length=255)


    def __str__(self):
        return self.title
