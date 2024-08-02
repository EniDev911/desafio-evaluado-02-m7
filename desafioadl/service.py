from .models import Tarea, SubTarea

todas = Tarea.objects.all()

def imprimir_en_pantalla(tareas=todas):
	for tarea in tareas:
		aux = 1
		print(tarea)
		for subtarea in tarea.subtarea_set.all():
			print(f"\t{aux}. {subtarea}")
			aux += 1
		print()


def crear_nueva_tarea():
	print("== Crear nueva Tarea ==")
	Tarea.objects.create(descripcion=input("Descripción de la nueva tarea:\n> "))

def crear_sub_tarea():
	print("== Crear nueva SubTarea ==")
	descripcion=input("Descripción de la nueva subtarea:\n> ")
	tarea_id = int(input("ID de la tarea a que pertenece:\n> "))
	SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)