#!/usr/bin/python

""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random

lugares_bote = []
viajes = 0
nb_places = threading.Semaphore(4)


def check_river_boca_in_bote(liste):
	boca = 0
	river = 0
	result = []
	for i in liste :
		if i == "R" :
			river += 1
		if i == "B" :
			boca += 1
	result.append(river)
	result.append(boca)
	return result


def a_bordo():
	global lugares_bote
	nb_places.acquire()
	if len(lugares_bote) == 4:
		a_remar()


def a_remar():
	global lugares_bote
	global viajes
	print "soy el capitan del viaje ",viajes," y me voy con mi embarcacion y tres companeros\n"
	lugares_bote = []
	nb_places.release()
	viajes += 1
	for i in range(4):
		nb_places.release()
	



def hincha_river():
   	""" Implementar funcion para subir al bote ....si es que se puede ..."""
	global lugares_bote
	boat = check_river_boca_in_bote(lugares_bote)
	if boat == [2,1]  or boat == [0,3] :
		print "Oh no puedo entrar !!!!"
	else :
		lugares_bote.append("R")
		print "vamos river ",lugares_bote
		a_bordo()


def hincha_boca():
	""" Implementar funcion para subir al bote ....si es que se puede ..."""
	global lugares_bote
	boat = check_river_boca_in_bote(lugares_bote)
	if boat == [1,2]  or boat == [3,0] :
		print "Oh no puedo entrar !!!!"
	else :
		lugares_bote.append("B")
		print "vamos boca ", lugares_bote
		a_bordo()


def barra_brava_river():
    	""" Generacion de hinchas de River"""
	while viajes < 20:
	        time.sleep(random.randrange(0, 5))
        	r = threading.Thread(target = hincha_river)
        	r.start()
        	r.join()

def barra_brava_boca():
	""" Generacion de hinchas de Boca"""
	while viajes < 20:
	        time.sleep(random.randrange(0, 5))
	        b = threading.Thread(target = hincha_boca)
	        b.start()
	        b.join()

t1 = threading.Thread(target = barra_brava_river)
t2 = threading.Thread(target = barra_brava_boca)

t1.start()
t2.start()


t2.join()
t1.join()
print("terminaron los viajes ")
