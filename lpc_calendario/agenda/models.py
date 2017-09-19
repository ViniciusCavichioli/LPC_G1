from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 150)
    email = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 12)
    endereco = models.CharField(max_length = 200)
    telefone = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    data = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nome)

class Agenda(models.Model):
    descricao = models.TextField()
    usuarios = models.ForeignKey(Usuario, null=True, blank=False)
    tiposAgenda = (u'privada',u'privada'), (u'publica',u'publica')
    tipo = models.CharField(max_length = 50, choices=tiposAgenda)
    compromissos = models.ManyToManyField(Compromisso)

    def __str__(self):
        return '{}'.format(self.nome)

class AgendaInstitucional(models.Model):
    feriados = models.ManyToManyField(Compromisso)
