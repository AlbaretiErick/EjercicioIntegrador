from Clase import Alumno
from Clase import ManejadorAlumnos
from Clase import ManejadorMaterias

if __name__ == '__main__':
    arregloAlumnos = ManejadorAlumnos (1)
    with open ('alumnos.csv', '+r') as archivo:
        for linea in archivo:
            p,a,r,t,e = linea.split (';')
            objeto = Alumno (p,a,r,t,e)
            arregloAlumnos.agregarAlumno (objeto)
    listaMaterias = ManejadorMaterias
    with open ('materiasAprobadas.csv', '+r') as archivo:
        for linea in archivo:
            materia = [linea.split (';')]
            listaMaterias = ManejadorMaterias (materia)
    print ('Seleccione una opción:\na - Informar el promedio de un alumno.\nb - Informar los estudiantes que la aprobaron en forma promocional.\nc - Mostrar un listado de alumnos.')
    opcion = input ('Opción: ')
    if opcion == 'a':
        dni = input ('Ingrese el DNI del alumno a buscar el promedio: ')
        bul = arregloAlumnos.buscarDni (dni)
        if bul == True:
            promedio = listaMaterias.getPromedio (dni)
            print ('El promedio del alumno es: {:.2f}'.format (promedio))
        else:
            print ('No se encontró el Alumno buscado.')
    elif opcion == 'b':
        materia = input ('Ingerse nombre de la materia: ')
        bul = arregloAlumnos.estudiantesAprobados (materia, listaMaterias)
        if bul == False:
            print ('La materia ingresada es erronea o no corresponde a una materia promocional.')
    elif opcion == 'c':
        arregloAlumnos.ordenar ()
        arregloAlumnos.mostrar ()
    else:
        print ('La opción ingresada no existe.')
    print ('Fin del programa...')