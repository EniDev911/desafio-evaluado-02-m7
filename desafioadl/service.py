from .models import Tarea, SubTarea
import os

def recupera_tareas_y_sub_tareas():
	print("== Recuperar tareas ==\n")
	tareas = Tarea.objects.filter(eliminada=True)
	if tareas.exists():
		for tarea_eliminada in tareas:
			print(f"Tarea ID: {tarea_eliminada.id} ({tarea_eliminada.descripcion})")
		tarea_id = input("Ingresa el ID de la tarea que desea recuperar:\n> ")
		tarea = Tarea.objects.filter(id=tarea_id)
		estado = tarea.update(eliminada=False) if tarea.exists() and tarea[0].eliminada == True else 0
		if estado == 1:
			tarea[0].subtarea_set.all().update(eliminada=True)
			return imprimir_en_pantalla()
		return "No existe la tarea o ya se recupero"
	print("No existen tareas eliminadas aún")

def crear_nueva_tarea():
	print("== Crear nueva Tarea ==\n")
	Tarea.objects.create(descripcion=input("Descripción de la nueva tarea:\n> "))
	imprimir_en_pantalla()

def crear_sub_tarea():
	print("== Crear nueva SubTarea ==\n")
	descripcion=input("Descripción de la nueva subtarea:\n> ")
	for tarea in Tarea.objects.filter(eliminada=False):
		print(f"Tarea ID: {tarea.id} ({tarea.descripcion})")
	tarea_id = int(input("ID de la tarea a que pertenece:\n> "))
	if Tarea.objects.filter(id=tarea_id).count() == 1:
		SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)
		return imprimir_en_pantalla()
	print("No existe la Tarea con ese ID\n")
	crear_sub_tarea()

def elimina_tarea():
	print("== Elimina una Tarea ==\n")
	imprimir_en_pantalla()
	tarea_id = int(input(f"ID tarea a eliminar:\n> "))
	tarea = Tarea.objects.filter(id=tarea_id)
	estado = tarea.update(eliminada=True) if tarea.exists() and tarea[0].eliminada == False else 0
	return imprimir_en_pantalla() if estado == 1 else "No existe la tarea o ya esta eliminada"

def elimina_sub_tarea():
	print("== Elimina una SubTarea ==\n")
	imprimir_en_pantalla()
	subtarea_id = int(input(f"ID de la subtarea a eliminar:\n> "))
	subtarea = SubTarea.objects.filter(id=subtarea_id)
	estado = subtarea.update(eliminada=True) if subtarea.exists() and subtarea[0].eliminada == False else 0
	return imprimir_en_pantalla() if estado == 1 else "No existe la subtarea o ya esta eliminada"

def imprimir_en_pantalla():
		print("== Mostrando Tareas y SubTareas Actuales ==\n")
		tareas = Tarea.objects.filter(eliminada=False)
		if tareas.count() == 0:
			return print("No existen tareas aún")
		for tarea in tareas:
			print(tarea)
			for subtarea in tarea.subtarea_set.all():
				if subtarea.eliminada == False:
					print(f"  {subtarea}")
			print()