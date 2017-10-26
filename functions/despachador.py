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
    hl1 = hls[0]
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

    if(nh>0):
        hls = [ cv.aeronave(100, 3, i) for i in range(nh) ]
        H = [ cv.agenda(hl) for hl in hls ]
    else:
        hls = []
        H = []

    if(nj>0):
        jts = [ cv.aeronave(140, 5, i) for i in range(nj) ]
        J = [ cv.agenda(jt) for jt in jts ]
    else:
        jts = []
        J = []

    for s in range(len(df)):
        reg = df.ix[s]
        sol = genera_solicitud(reg)
        r = procesa_solicitud(sol, nh, nj, H, J)

        df.ix[s,'status'] = r

    df.to_csv('demanda_procesada.csv')

