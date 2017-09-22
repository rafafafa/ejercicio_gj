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
    def tiempo_crucero(self, d):
        """
        Calcula el tiempo crucero en el que
        esta aeronave recorre la distancia d
        """
        tc = d / self.__vc
        return tc
    def calcula_tiempo(self, d1, d2):
        """
        Calcula el tiempo en el que
        esta aeronave recorre la distancia
        |d1-d2|
        """
        dt = abs(d2-d1)
        tc = self.tiempo_crucero(dt)
        return tc


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
        self.__actual = 0
    def __siguiente_evento_idx(m):
        L = self.__A.keys()
        maxi = len(L) - 1
        if(m<maxi):
            return L[m+1]
        else:
            return -1
    def __genera_rango(self, m, r=4, s=0.25, factor=3600):
        """
        Calcula un rango de tiempo centrado en m
        de radio r con un step s
        El factor multiplica a m-r y s para dejarlos
        en las mismas unidades. Es decir, ambos
        deben estar en la misma unidad temporal
        """
        R = set(range(m-r*factor, m+r*factor, int(s*factor)))
        return R
    def __ocupados(self, m):
        """
        Determina los lugares ocupados en la agenda
        centrados en la hora m y con un rango de 4 horas
        """
        R = self.__genera_rango(m)
        L = self.__A.keys()
        D = R.intersection(L)
        return list(D)
    def __hora_libre(m,k,r=4):
        """
        Función booleana que regresa True
        si m es una hora libre de tamaño k
        """
        D = self.__A
        R = D.get(m,1)
        if(R==1): #no existe agendado, falta checar que quepa
            K = self.__rango(m)
            #asignamos temporalmente el ticket
            D[m] = 'temporal'
            idxsig = self.__siguiente_evento_idx(m)
            Sig = D[idxsig] #evento siguiente al planeado en m
            Ts,hr,an = Sig
            if(m+k>=hr):
                return False
            else:
                return True
    def agenda_vuelo(self, T,hr,an):
        """
        Método que agenda el ticket T
        en la hora hr con la aeronave an
        """
        if(self.cabe_vuelo(T,hr,an)):
            A[T] = (T, hr, an)
            return 1
        else:
            return 0
    def cabe_vuelo(self, T, an):
        """
        Determina con True/False si el ticket T
        se puede establecer en su hora de vuelo
        T.hora_vuelo
        """
        m = T.hora_vuelo
        d = T.distancia
        tc = an.tiempo_crucero(d)
        print("incompleto")







#diccionario de aeronaves
A = {1:aeronave(100, 3,'XXX'), 2:aeronave(140, 5, 'YYY')}



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

