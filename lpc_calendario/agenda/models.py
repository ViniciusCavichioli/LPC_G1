from django.db import models
from django.contrib.auth.models import User

class Agenda(models.Model):
    visivel = models.BooleanField(True, verbose_name = "Visivel")
    descricao = models.TextField()
    usuario = models.ManyToManyField(User)
    tipo = models.CharField(max_length = 100)
    institucional = models.BooleanField(True, verbose_name = "Institucional")

    def __str__(self):
        return '{}'.format(self.tipo)

class Compromisso(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    dataHoraInicio = models.DateTimeField(blank=True, null=True)
    dataHoraFim = models.DateTimeField(blank=True, null=True)
    agendas = models.ForeignKey(Agenda, null=True, blank=False)

    def __str__(self):
        return "{}".format(self.nome)
