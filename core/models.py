from django.db import models
from Comuns.models import Pais,Estado, Cidade

class Clube(models.Model):

    DIVISAO_CHOICES = (
    ('A', '1º DIVISÃO'),
    ('B', '2ª DIVISÃO'),
    ('C', '3º DIVISÃO'),
    ('D', '4º DIVISÃO'),    
)
    
    MODALIDADE_CHOICES = (
    ('F', 'FEMININA'),
    ('M', 'MASCULINA'),  
)


    nome = models.CharField(max_length=120)
    ano_de_fundacao = models.PositiveIntegerField(default=0)
    divisao = models.CharField(choices=DIVISAO_CHOICES, null=False, max_length=100, blank=True)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)
    
    modalidade = models.CharField(choices=MODALIDADE_CHOICES,max_length=90,null=False,blank=True)
    cores = models.CharField(max_length=80, blank=True, null=True)
    tem_mundial = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True,blank=True)

    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural='Clubes'

class Jogador(models.Model):
    POSICAO_CHOICES = (
    ('ATC', 'ATACANTE'),
    ('DEF', 'ZAGUEIRO'),
    ('LAT', 'LATERAL'),     
)

    SEXO_CHOICES = (
    ('F', 'FEMININO'),
    ('M', 'MASCULINO'),  
)

    nome = models.CharField(max_length=120)
    foto = models.ImageField(upload_to="images/",null=True,blank=True)
    clube = models.ForeignKey(Clube,on_delete=models.CASCADE,null=True)
    posicao = models.CharField('POSIÇÃO',choices=POSICAO_CHOICES,max_length=100,null=True)
    numero_da_camisa = models. IntegerField('NÚMERO',null=False)
    sexo = models.CharField(choices=SEXO_CHOICES,max_length=80,null=True) 
 
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural='Jogadores'

class Competicao(models.Model):
    TIPO_CHOICES = (
    ('E', 'ESTADUAL'),
    ('N', 'NACIONAL'),
    ('I', 'INTERNACIONAL'),           
)
    CATEGORIA_CHOICES =(
    ('CP', 'COPA'),
    ('CAMP', 'CAMPEONATO'),        
)

    nome = models.ForeignKey(Clube,on_delete=models.CASCADE,max_length=120)
    tipo = models.CharField(choices=TIPO_CHOICES,max_length=80,null=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES,max_length=80,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural='Competições' 

class Titulo(models.Model):
    COLOCACAO_CHOICES = (
    ('1º', 'CAMPEÃO'),
    ('2ª', 'VICE')    
)

    ano_da_conquista = models.PositiveIntegerField(default=0)
    data_exata = models.DateField(null=True,blank=True)
    colocacao = models.ForeignKey(Clube,on_delete=models.CASCADE,choices=COLOCACAO_CHOICES,max_length=80,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural='Títulos'