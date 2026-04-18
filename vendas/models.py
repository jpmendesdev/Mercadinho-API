from django.db import models
from produto.models import Produto
from usuarios.models import Usuario

class Venda(models.Model):
    STATUS = {
        'atv':'ativo',
        'des':'desativo'
    }
    qtd_de_produtos = models.IntegerField()
    valor_total = models.DecimalField(decimal_places=2,max_digits=5,default=000.00)
    produtos = models.ManyToManyField(Produto)
    status = models.CharField(default=STATUS['atv'],choices=STATUS)
    usuario_fk = models.ForeignKey(
         Usuario,
         on_delete=models.CASCADE,
         null=True
     )
    #cliente

