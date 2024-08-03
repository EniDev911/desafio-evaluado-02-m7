from .models import Tarea, SubTarea


def recupera_tareas_y_sub_tareas():
	print("== Recuperar tareas ==")
	tareas = Tarea.objects.filter(eliminada=True)
	if tareas.exists():
		for tarea_eliminada in tareas:
			print(f"Tarea ID: {tarea_eliminada.id} ({tarea_eliminada.descripcion})")
		id_tarea = input("Ingresa el ID de la tarea que desea recuperar:\n> ")
		Tarea.objects.filter(id=id_tarea).update(eliminada=False)
		return imprimir_en_pantalla() 
	print("No existen tareas eliminadas aún")

def crear_nueva_tarea():
	print("== Crear nueva Tarea ==")
	Tarea.objects.create(descripcion=input("Descripción de la nueva tarea:\n> "))

def crear_sub_tarea():
	print("== Crear nueva SubTarea ==")
	descripcion=input("Descripción de la nueva subtarea:\n> ")
	for tarea in Tarea.objects.filter(eliminada=False):
		print(f"Tarea ID: {tarea.id} ({tarea.descripcion})")
	tarea_id = int(input("ID de la tarea a que pertenece:\n> "))
	if Tarea.objects.filter(id=tarea_id).count() == 1:
		SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)
	else:
		print("No existe la Tarea con ese ID\n")
		crear_sub_tarea()

def elimina_tarea():
	id_tarea = int(input("ID tarea a eliminar\n> "))
	Tarea.objects.filter(id=id_tarea).update(elimina=True)
	imprimir_en_pantalla()


def elimina_sub_tarea():
	pass

def imprimir_en_pantalla():
		tareas = Tarea.objects.filter(eliminada=False)
		if tareas.count() == 0:
			return print("No existen tareas aún")
		for tarea in tareas:
			aux = 1
			print(tarea)
			for subtarea in tarea.subtarea_set.all():
				if not tarea.eliminada:
					print(f"\t{aux}. {subtarea}")
					aux += 1
			print()