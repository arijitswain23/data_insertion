from django.db import models

# Create your models here.
class State(models.Model):
    Sno=models.BigIntegerField(max_length=2,primary_key=True)
    State_name=models.CharField(max_length=100)
    Capital=models.CharField(max_length=100)
    def __str__(self):
        return self.State_name
class Capital(models.Model):
    State_name=models.ForeignKey(State,on_delete=models.CASCADE)
    Cno=models.BigIntegerField(max_length=3,primary_key=True)
    Capital_name=models.CharField(max_length=100)
    Population=models.BigIntegerField(max_length=3)
    def __str__(self):
        return self.Capital_name
