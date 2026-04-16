from django.db import models

class Setor(models.Model):
    STATUS = {
        'active':'ativo',
        'deactivate':'desativado'
    }
    nome = models.CharField(default='',max_length=30)
    max_produtos = models.IntegerField(default=1)
    status = models.CharField(default='ativo',choices=STATUS)

    def __str__(self):
        return self.nome