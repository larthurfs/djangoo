from django.db import models

class Ferramentas(models.Model):

    nome = models.CharField(max_length=50, unique=True, blank=True, null=True)
    ativa = models.BooleanField(default=False)


    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'db_ferramentas_cadastradas'
        verbose_name_plural = 'BD Ferramentas Cadastradas'
        verbose_name = 'BD Ferramentas Cadastradas'

