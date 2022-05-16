from django.db import models

class Symbol(models.Model):
    symbol = models.CharField(max_length=10)
    
    def __str__(self):
        return self.symbol
    
from django.db import models  
class List(models.Model):  
    item = models.CharField(max_length=200)
    alert_code = models.CharField(max_length=200)
    severity = models.CharField(max_length=200)
    agency = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    class Meta:  
        db_table = "list"
        
    def __str__(self):
        return self.item