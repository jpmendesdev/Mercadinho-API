from django.db import models
from setor.models import Setor

class Produto(models.Model):
    TIPOS = {
        'PRO':'processados',
        'LAT':'laticínios',
        'CAR':'carnes',
        'BEB':'bebidas',
        'LIM':'produtos de limpeza',
        'PLA':'plásticos'
    }
    nome = models.CharField(max_length=255)
    tipo = models.CharField(default='',choices=TIPOS,max_length=3)
    descricao = models.TextField(blank=True)
    quantidade = models.IntegerField()
    setor_fk = models.ForeignKey(
        Setor,
        on_delete=models.PROTECT,
    )
    status = models.BooleanField(default=True)
    preco_de_custo = models.DecimalField(max_digits=5,decimal_places=2,default=000.00)
    preco_de_venda = models.DecimalField(max_digits=5,decimal_places=2,default=000.00)
    data_de_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}, do tipo {self.tipo}"
