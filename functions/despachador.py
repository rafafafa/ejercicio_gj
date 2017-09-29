#!/usr/bin/python2.7
#coding:utf8

import pandas as pd
import sys
import calendarizador_vuelos as cv
from random import choice, shuffle

def genera_solicitud(reg):
    m = reg.fvn
    n = reg.fsn
    o = (reg.o_lat, reg.o_lon)
    d = (reg.d_lat, reg.d_lon)
    return cv.ticket(m, n, o, d)

def procesa_solicitud(sol, nh, nj, H, J):
    Aj = J[:nj]
    Ah = H[:nh]
    if(hl1.tiempo_crucero(sol.distancia)>2):
        for j in Aj:
            r = j.agenda_vuelo(sol)
            if(r==1): break
        return r
    else:
        A = Aj + Ah
        shuffle(A)
        for h in A:
            r = h.agenda_vuelo(sol)
            if(r==1): break
        return r



if __name__ == '__main__':
    nh = int(sys.argv[1])
    nj = int(sys.argv[2])
    df = pd.read_csv('demanda.csv')

    hl1 = cv.aeronave(100, 3,'R66')
    hl2 = cv.aeronave(100, 3,'R67')
    jt1 = cv.aeronave(140, 5,'VPA 34')
    jt2 = cv.aeronave(140, 5,'VPA 35')

    if(nh==2):
        H = [ cv.agenda(hl1), cv.agenda(hl2) ]
    elif(nh==1):
        H = [ cv.agenda(hl1) ]

    if(nj==2):
        J = [ cv.agenda(jt1), cv.agenda(jt2) ]
    elif(nj==1):
        J = [ cv.agenda(jt1) ]

    for s in range(len(df)):
        reg = df.ix[s]
        sol = genera_solicitud(reg)
        r = procesa_solicitud(sol, nh, nj, H, J)

        df.ix[s,'status'] = r

    df.to_csv('demanda_procesada.csv')

