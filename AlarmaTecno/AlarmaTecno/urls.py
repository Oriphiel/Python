#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Edgar Arturo Haas Pacheco
# @Date:   2015-10-04 ‏‎‏‎19:49:33

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from AlarmaTecno.settings import STATIC_ROOT_DEVELOPMENT

admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'untitled3.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT_DEVELOPMENT,
                                                                           'show_indexes': True}),
                       url(r'^admin/', include(admin.site.urls), name='administrador'),
                       url(r'^mantenimiento/listadia/$', 'Alarma.views.inicio', name='listadia'),
                       url(r'^sonar/(?P<tipo>[\w]+)$', 'Alarma.views.alarm', name='sonar'),
                       url(r'^mantenimiento/agregar/$', 'Alarma.views.agregar', name='agregar'),
                       url(r'^mantenimiento/$', 'Alarma.views.listatimbres', name='mantenimiento'),
                       url(r'^mantenimiento/tiempo/$', 'Alarma.views.tiempo', name='proxima'),
                       url(r'^mantenimiento/(?P<id_tiempo>[^/]+)/borrar/$', 'Alarma.views.borrar', name='borrar'),
                       url(r'^mantenimiento/(?P<id_tiempo>[^/]+)/status/inactive$', 'Alarma.views.change_status',
                           name='status'),
                       url(r'^mantenimiento/(?P<id_tiempo>[^/]+)/status/active$', 'Alarma.views.change_status_active',
                           name='active'),
                       url(r'^mantenimiento/(?P<id_tiempo>[^/]+)/update/$', 'Alarma.views.update', name='update'),
                       url(r'^$', 'Alarma.views.index', name='inicio'),
                       url(r'^salir/$', 'Alarma.views.logout_usuario', name='signout'),
                       url(r'^login/$', 'Alarma.views.login_usuario', name='login'),
                       url(r'^inicio/$', 'Alarma.views.principal', name='inicio'),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
