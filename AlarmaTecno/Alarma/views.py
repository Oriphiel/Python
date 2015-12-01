#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-04 ‏‎‏‎19:49:33

from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Alarma.forms import TiempoForm
from Alarma.models import Tiempo
from Alarma.timbre import estado
from Alarma.tiempo import bases, comprobar, allday

# Create your views here.


def index(request):
    if request.user.is_authenticated():
        return principal(request)
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))


@login_required(login_url='/')
def inicio(request):
    if comprobar():
        days = allday()
        return render_to_response('lista.html', {'day': days}, context_instance=RequestContext(request))
    else:
        days = None
        return render_to_response('lista.html', {'day': days}, context_instance=RequestContext(request))


@login_required(login_url='/')
def principal(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))


def login_usuario(request):
    control = request.user.is_authenticated()
    if control:
        return principal(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return principal(request)

    return render_to_response('index.html', context_instance=RequestContext(request))


@login_required(login_url='/')
def logout_usuario(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def alarm(request, tipo):
    if request.user.is_superuser:
        if request.POST:
            state = int(request.POST.get('optradio'))
            estado(state)
        return render_to_response('alarma.html', {'alarma': int(tipo)}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def agregar(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            if len(request.POST.getlist('dias')) > 0 and len(request.POST.get('hora')) > 0 and len(request.POST.get('minuto')) > 0\
                    and len(request.POST.get('optradio')) > 0:
                tiempo_hora = request.POST.get('hora')
                tiempo_minuto = request.POST.get('minuto')
                tiempo_tipo = int(request.POST.get('optradio'))
                for dias in request.POST.getlist('dias'):
                    formulario = TiempoForm({'tiempo_dia': int(dias), 'tiempo_hora': tiempo_hora, 'tiempo_minuto': tiempo_minuto,
                                             'tiempo_tipo': tiempo_tipo})
                    if formulario.is_valid():
                        formulario.save()

                return HttpResponseRedirect('/mantenimiento/')

            else:
                return render_to_response('agregarmejorado.html', context_instance=RequestContext(request))
        else:
            return render_to_response('agregarmejorado.html', context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def listatimbres(request):
    if request.user.is_superuser:
        objetos = Tiempo.objects.all().order_by('tiempo_dia', 'tiempo_hora', 'tiempo_minuto')
        return render_to_response('crud_lista.html', {'lista': objetos}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def tiempo(request):
    if comprobar():
        objeto = bases()
        return render_to_response('tiempo.html', {'lista': objeto}, context_instance=RequestContext(request))
    else:
        objeto = None
        return render_to_response('tiempo.html', {'lista': objeto}, context_instance=RequestContext(request))


@login_required(login_url='/')
def borrar(request, id_tiempo):
    if request.user.is_superuser:
        objeto = Tiempo.objects.all().get(pk=id_tiempo)
        objeto.delete()
        return HttpResponseRedirect('/mantenimiento/')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def update(request, id_tiempo):
    if request.user.is_superuser:
        tiempopagina = Tiempo.objects.all().get(pk=int(id_tiempo))
        if request.method == 'POST':
            tiempo_dia = request.POST.get('dia')
            tiempo_hora = request.POST.get('hora')
            tiempo_minuto = request.POST.get('minuto')
            tiempo_tipo = int(request.POST.get('optradio'))
            formulario = TiempoForm({'tiempo_dia': tiempo_dia, 'tiempo_hora': tiempo_hora, 'tiempo_minuto': tiempo_minuto,
                                     'tiempo_tipo': tiempo_tipo}, instance=tiempopagina)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect('/mantenimiento/')
            else:
                return render_to_response('update.html', {'tiempo': tiempopagina}, context_instance=RequestContext(request))
        else:
            return render_to_response('update.html', {'tiempo': tiempopagina}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def change_status(request, id_tiempo):
    if request.user.is_superuser:
        tiempopagina = Tiempo.objects.get(pk=int(id_tiempo))
        tiempopagina.tiempo_status = 'Inactive'
        tiempopagina.save()
        return HttpResponseRedirect('/mantenimiento/')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/')
def change_status_active(request, id_tiempo):
    if request.user.is_superuser:
        tiempopagina = Tiempo.objects.get(pk=int(id_tiempo))
        tiempopagina.tiempo_status = 'Active'
        tiempopagina.save()
        return HttpResponseRedirect('/mantenimiento/')
    else:
        return HttpResponseRedirect('/')
