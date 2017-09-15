#!/usr/bin/python
#coding:utf8

import sys
from math import sin, cos, atan2,sqrt, radians

class aeronave(object):
    def __init__(self, vc, c, matricula):
        self.__vc = vc
        self.__c  = c
        self.__m  = matricula
    @property
    def velocidad_crucero(self): return self.__vc
    @property
    def capacidad(self): return self.__c
    @property
    def id(self): return self.__m

class ticket(object):
    def __init__(self, n,m,o,d):
        self.__hr = n
        self.__hv = m
        self.__origen  = o
        self.__destino = d
        self.__calcula_distancia()
    def __haversine(self,c1,c2):
        """
        Calcula las distancia de Haversine entre c1 y c2
        """
        lat1,lon1 = c1
        lat2,lon2 = c2
        R = 6371
        dlat = radians(lat2)-radians(lat1)
        dlon = radians(lon2)-radians(lon1)
        a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) \
            * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R*c
        return d;
    @property
    def hora_viaje(self): return self.__hv
    @property
    def hora_reserva(self): return self.__hr
    @property
    def origen(self): return self.__origen
    @property
    def destino(self): return self.__destino
    def __calcula_distancia(self):
        d = self.__haversine(self.__origen,self.__destino)
        self.__distancia = d
    @property
    def distancia(self):
        return self.__distancia

class agenda(object):
    """
    Objeto para manejar la agenda de vuelos
    creado a partir de objetos tipo ticket.
    Contiene los métodos agenda_vuelo(T)
    que establece el vuelo a la hora (T.hora_viaje)
    y el metodo cabe_vuelo(T) que determina si
    el vuelo de T.origen a T.destino puede establecerse
    en T.hora_vuelo
    """
    def __init__(self):
        self.__A = dict()
    def agenda_vuelo(self, T):
        A[T.hora_viaje] = T
    def cabe_vuelo(self, S, T, an, th):
        """
        Determina con True/False si el ticket T
        se puede establecer en su hora de vuelo
        T.hora_vuelo
        """
        m = T.hora_vuelo
        d = T.distancia
        cabe = cabe_viaje(m,T.origen, T.destino, an, th)
        if(cabe):
            return True
        else:
            return False


#diccionario de aeronaves
A = {1:aeronave(100, 3,'XXX'), 2:aeronave(140, 5, 'YYY')}

#diccionario de


def calcula_tiempo(d1,d2,an):
    """
    Funcion que calcula el tiempo en
    el que la aeronave an recorre
    |d2-d1|
    """
    vc = an.velocidad_crucero
    d = abs(d2-d1)
    t = d/vc
    return t

def cabe_viaje(hi, origen, destino, an, th):
    tiempo = calcula_tiempo(origen,destino,an)
    if(hi + tiempo<=th):
        return True
    else:
        return False

def agenda_ticket( t ):
    """
    Recibe un ticket t (diccionario) que
    contiene
    {n:valor, m: valor, o:origen, d:destino}
    para asignarle una aeronave de todas
    las posibles aeronaves
    """


if __name__ == '__main__':
    pass

