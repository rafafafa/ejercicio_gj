#!/usr/python
#coding:utf8

import calendarizador_vuelos as cv

hl = cv.aeronave(100, 3,'R66')
jt = cv.aeronave(140, 5, 'VPA 34')
A = {'hl':hl, 'jt':jt}

#Definiendo un ticket nuevo
T = cv.ticket(100,100,(19.24647,-99.10135),(20.593056,-100.392222))
org = T.origen
dst = T.destino
print("Ticket con origen {0} y destino {1}".format(org,dst))
d = T.distancia
print("La distancia entre el origen y el destino es {0}".format(d))
print("La hora de salida es {0}".format(T.hora_viaje))
print("El vuelo fue reservado en {0}".format(T.hora_reserva))

S = cv.ticket(120,120, (20.593056,-100.392222), (19.24647,-99.10135))
org2 = S.origen
dst2 = S.destino
print("Ticket con origen {0} y destino {1}".format(org,dst))
d2 = S.distancia
print("La distancia entre el origen y el destino es {0}".format(d2))
print("La hora de salida es {0}".format(S.hora_viaje))
print("El vuelo fue reservado en {0}".format(S.hora_reserva))

#Definiendo una agenda
G = cv.agenda()
print("Agendando T en la agenda G")
G.agenda_vuelo(T)
print("Determinando si el vuelo S puede ser agendado en G con la aeronave {0}".format(A['jt'].id))
c = G.cabe_vuelo(S,T,A['jt'],1)



