from django.db import models


class Pais(models.Model):
    pais = models.CharField(max_length=80, null=True)
    
    def __str__(self):
        return self.pais

    class Meta:
        verbose_name_plural='PAÍSES'
    
class Estado(models.Model):
    estado = models.CharField(max_length=80, null=True)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE, null=True) 
     
    def __str__(self):
        return self.estado

    class Meta:
        verbose_name_plural='ESTADOS'
     
class Cidade(models.Model):
    cidade = models.CharField(max_length=80, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.cidade

    class Meta:
        verbose_name_plural='CIDADES'
           