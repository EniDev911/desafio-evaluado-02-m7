from .models import Tarea

def base_data(cls):
    cls.Tarea1 = Tarea.objects.create(
       descripcion="first_descripcion"
    )
    cls.Tarea1.subtarea_set.create(descripcion="An subtarea")
    
    cls.Tarea2 = Tarea.objects.create(
       descripcion="second_descripcion"
    )