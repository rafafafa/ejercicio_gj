#!/usr/bin/python
#coding:utf8

import sys
from math import sin, cos, atan2, sqrt, radians
from numpy import argmin, argsort

class aeronave(object):
    def __init__(self, vc, c, matricula):
        self.__vc = vc   #vel crucero
        self.__c  = c    #capacidad
        self.__m  = matricula #id
    def __str__(self):
        return str(self.__m)+" "+str(self.__c)+" "+str(self.__vc)
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
        """
        Clase ticket o solicitud de vuelo
        Se instancia con
        (hora reserva, hora deseada de viaje, origen y destino)
        """
        self.__hr = n
        self.__hv = m
        self.__origen  = o
        self.__destino = d
        self.__calcula_distancia()
    def __str__(self):
        cad = "m:" + str(self.__hv) + \
              " - n:" + str(self.__hr) + \
              " - o:" + str(self.__origen) + \
              " - d:"+str(self.__destino)
        return cad
    @staticmethod
    def haversine(c1,c2):
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
        d = self.haversine(self.__origen,self.__destino)
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
    def __init__(self, an, tick=900, dur=30 ):
        """
        Genera una agenda con duracion dur (30) días
        que deben ser convertidos a segundos
        y cada paso es de 900 segundos.

        """
        self.__an   = an #aeronave
        self.__A    = dict() #eventos anotados
        self.__T    = dur*24*60*60 #duracion de la simulación en segundos
        self.__tick = tick
        self.__P    = set(range(0,self.__T,tick)) #puntos posibles agendables
        self.__M    = set(range(0,self.__T,tick))
    def __str__(self):
        cad = ''
        L = self.__A.keys()
        if(len(L)>0):
            for k,v in self.__A.iteritems():
                cad += str(k)+": ["+','.join(map(str,v))+"]\n"
        else:
            cad = 'Agenda vacia'
        return cad
    def __siguiente_evento_idx(self, m):
        """
        Da el indice en el diccionario que tiene el siguiente evento posible
        Si respuesta es -2 entonces no hay eventos registrados
        Si respuesta es -1 entonces es el final de la lista
        """
        L = self.__A.keys()
        if(len(L)>0):
            try:
                idx = L.index(m)
            except:
                return -2
            if(idx==len(L)-1):
                return L[idx]
            else:
                return L[idx+1]
        else:
            return -2
    def __genera_rango(self, m, r=4, factor=3600):
        """
        Calcula un rango de tiempo centrado en m de radio r con un step s
        El factor multiplica a m-r y s para dejarlos en las mismas unidades.
        Es decir, ambos deben estar en la misma unidad temporal
        """
        s = self.__tick
        R = set(range(m-(r*factor), (m+1)+(r*factor), s))
        return R
    def __ocupados(self, m):
        """
        Determina los lugares ocupados en la agenda
        centrados en la hora m y con un rango de 4 horas
        """
        R = self.__genera_rango(m)
        D = self.__P.intersection(R)
        D = R.difference(D)
        return sorted(list(D))
    def ocupados(self, m):
        return self.__ocupados(m)
    def libres(self,m):
        """
        Determina todos los lugares libres en la agenda
        centrados en la hora m y con un rango de 4 horas
        """
        R = self.__genera_rango(m)
        #print("libres {0}".len(R))
        L = R.intersection(self.__P)
        return sorted(list(L))
    def __cabe_vuelo(self, T, hs, R):
        """
        Determina con True/False si el ticket T se puede establecer
        en su hora de vuelo en la hora sugerida hs
        """
        A = self.__A   #copia de la agenda
        K = A.keys()   #llaves de los eventos agendados
        an = self.__an #aeronave
        ed = R[-1]     #extremo derecho del intervalo R
        m, n, o, d = T.hora_viaje, T.hora_reserva, T.origen, T.destino
        iS = [ i for i in K if i > hs ]
        #print "ed {0}".format(ed)," "
        if(len(iS)>0):
            isig = iS[0]
            S = A[isig]
            Tk, hk = S
            ok, _ = Tk.origen, Tk.destino
            dk = ticket.haversine(d,ok)
            dm = ticket.haversine(o,d)
            tc = an.tiempo_crucero(dk+dm)
            if(hs+tc > hk):
                return False
            else:
                return True
        else:
            tc = an.tiempo_crucero(T.distancia)
            if(hs+tc > ed):
                return False
            else:
                return True
    def __busca_cercano(self, m):
        """
        Método que busca dentro de los puntos libres
        el más cercano al segundo m dentro del rango
        de +-4 horas
        """
        L = list(sorted(self.__M))
        idx = argmin([abs(m-x) for x in L])
        return L[idx]
    def cercano(self, m):
        p =  self.__busca_cercano(m)
        return p
    def cabe(self, T, R):
        """
        Se establece la solicitud T en el espacio
        en el que quepa más cercano a su hora de
        vuelo deseada
        """
        m = T.hora_viaje
        L = sorted(list(R))
        I = []
        #for i in range(len(L)):
        #    if(self.__cabe_vuelo(T,L[i], L)):
        #        I.append(L[i])
        for r in L:
            #print r," ",
            if(self.__cabe_vuelo(T,r,L)):
                I.append(r)
        I = [L[r] for r in argsort([abs(m-x) for x in L])]
        return I
    def agenda_vuelo(self, T, s=3600):
        """
        Método que agenda el ticket T
        en la hora hr con la aeronave an
        """
        dist     = T.distancia
        an       = self.__an
        duracion = int(an.tiempo_crucero(dist)*s)+1 #porque el tiempo está en horas
        #print(duracion)
        m        = T.hora_viaje
        #print("hora deseada: {0}".format(m))
        cm       = self.cercano(m)
        #print("punto cercano {0}".format(cm))
        R        = self.__genera_rango(cm)
        #print("rango previo {0}".format(sorted(list(R))))
        V = []
        for r in R:
            try:
                if(list(self.__P).index(r)>0):
                    V.append(r)
            except:
                pass
        W = set(V)
        #print("validos {0}".format(W))
        L        = self.cabe(T, V)
        #print("cabe: "+str(L))
        if(len(L)>0):
            pm = L[0]
            self.__A[pm] = (T, pm)
            #print("quitando {0}".format(R))
            self.__P     = self.__P.difference(R)
            #print("longitud de libres P {0} y totales M {1}".format(len(self.__P),len(self.__M)))
            #print(">>>>>>>>>>>> 1")
            return 1
        else:
            #print(">>>>>>>>>>>> 0")
            return 0


#diccionario de aeronaves

if __name__ == '__main__':
    pass

