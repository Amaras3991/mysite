from django.db import models

class CostumerInfo(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.FloatField()
    pub_date = models.DateTimeField("Data published")

    def __str__(self):
        return (f"{self.name} {self.last_name}")
