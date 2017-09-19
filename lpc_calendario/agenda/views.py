from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agenda.objects.all()
    for age in lista:
        retorno += '</br> Agendas: {} </br>'.format(Agenda.usuarios, Agenda.tipo)
    return HttpResponse(retorno)

def get_evento_byID(request, id):
    retorno = "<h1>Agenda do Usuario</h1>"
    lista = Agenda.objects.filter(usuario_id=id)
    if agenda.tipo=="publica":
        retorno += '</br> Agenda Publica: {}</br>'.format(Agenda.usuario)
    return HttpResponse(retorno)

def listaFeriado(request):
    lista = AgendaInstitucional.objects.all()
    retorno=''
    for ai in lista:
        retorno += '<p>Agenda Institucional: </p>'
        listaa = Feriados.feriados.all()
        retorno += '<p>Feriados: <ul>'
        for c in listaa:
            retorno += '<li>{}, {}</li>'.format(compromossi.nome, compromisso.data)
    return HttpResponse(retorno)
