#!/usr/python
#coding:utf8
import sys
import calendarizador_vuelos as cv
import pandas as pd

hl = cv.aeronave(100, 3,'R66')
jt = cv.aeronave(140, 5, 'VPA 34')
A = {'hl':hl, 'jt':jt}

#Definiendo un ticket nuevo
S = cv.ticket(120,120, (20.593056,-100.392222), (19.24647,-99.10135))
T = cv.ticket(100,100,(19.24647,-99.10135),(20.593056,-100.392222))
U = cv.ticket(882900,882900,(19.24647,-99.10135),(20.593056,-100.392222))
W = cv.ticket(1808,1808,(19.24647,-99.10135),(20.593056,-100.392222))

#Definiendo una agenda para el helicóptero
H = cv.agenda(hl)
J = cv.agenda(jt)

print(H)
print("Vuelo T")
r = H.agenda_vuelo(T)
print("r: {0}".format(r))
print(H)
print("Otra vez vuelo T")
r = H.agenda_vuelo(T)
print("r: {0}".format(r))
print(H)
print("Vuelo S")
r = H.agenda_vuelo(S)
print("r: {0}".format(r))
print(H)
print("Vuelo U")
r = H.agenda_vuelo(U)
print("r: {0}".format(r))
print(H)
print("Vuelo W")
r = H.agenda_vuelo(W)
print("r: {0}".format(r))
print(H)
print("Otro Vuelo W")
r = H.agenda_vuelo(W)
print("r: {0}".format(r))
print(H)


if __name__=='__main__':
    #nh = int(sys.argv[1])
    #nj = int(sys.argv[2])
    #df = pd.read_csv('demandas.csv')
    pass


