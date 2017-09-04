# Programa simple de calculador de propinas
import msvcrt

def costo():
	impuestos = 21 / 100
	propina = 10.0 / 100
	print ("Bienvenid@ al calculador de propinas, que calcula el total a pagar de su plato con I.V.A., y además le dice cuánto es el mínimo que, generosidad mediante, debería dejársele a el/la amable moz@ que l@ atendió.")
	print ("")
	comida = input("Ingrese el costo de el plato que ordenó, sólo dígitos: ")
	print("")
	total = float(comida) + float(comida) * impuestos
	print("$" + "%.2f" % total + " con I.V.A. incluído.")
	print("La propina es: $" + str("%.2f" %(total * propina)))
	print("Programado por Antonio Ortega")
	print("Pulse cualquier tecla para salir.")
	while True:
		if msvcrt.kbhit():
			break
	

costo()
