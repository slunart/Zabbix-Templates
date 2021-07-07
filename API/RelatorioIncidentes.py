# -*- coding: utf-8 -*-

from zabbix_api import ZabbixAPI
import datetime
import sys
import re

URLZABBIX=""
USUARIO=""
SENHA=""
GRUPO=""

zapi = ZabbixAPI(server=URLZABBIX)
zapi.login(USUARIO, SENHA)

print("===================== LISTA DOS INCIDENTES ====================")
print(datetime.datetime.now())

grupoX = zapi.hostgroup.get({
        "output": [
                "id"
        ],
        "search": {
                "name": [GRUPO],
        },
        "searchWildcardsEnabled": True,

})

id =  grupoX[0]['groupid']

eventos = zapi.problem.get({
        "output": [
                "eventids",
                ],
        "groupids": id,
        "severities": 4,
})

eventosXSeveridadeAlta = []
for e in eventos:
        eventosXSeveridadeAlta.append(e["eventid"])

hostsComEventos = zapi.event.get({
        "output": [
                "name",
                ],
        "eventids": eventosXSeveridadeAlta,
        "selectHosts": ["name"],
})

hostsComAlarmes = []
for h in hostsComEventos:
        hostsComAlarmes.append(h['hosts'][0]['hostid'])

hostsComAlarmeX = zapi.host.get({
        "output": [
                "name"
        ],
        "hostids": hostsComAlarmes,
        "searchWildcardsEnabled": True,
})

print("Qtde de hosts de DO GRUPO X com eventos de Severidade Alta")
print(len(hostsComAlarmeX))

hostsTotal = zapi.host.get({
        "output": [
                "name"
        ],
        "groupids": id,
        "searchWildcardsEnabled": True,
})

print("Qtde Total de hosts")
print(len(hostsTotal))


zapi.logout()
print("Tarefa Finalizada.\n")
