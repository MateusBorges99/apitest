from django.db import models

class pagamento(models.Model):
   
             id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
             data_pagamento = models.DateField(auto_now_add=True)
             permite_recorrencia =  models.BooleanField((""))
             quantidade_recorrencia =  models.IntegerField((""))
             intervalo_recorrencia = models.IntegerField((""))
             status_recorrencia = models.TextField((""))
             agencia = models.IntegerField((""))
             conta = models.IntegerField((""))
             valor = models.DecimalField(max_digits=10, decimal_places=2)  
  
             def save(self, *args, **kwargs):  
              self.valor = int(self.valor)  
              super().save(*args, **kwargs)
             
    
             
             
             
             

    

    