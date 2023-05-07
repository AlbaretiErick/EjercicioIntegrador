import numpy as np

class Alumno:
    __dni = None
    __apellido = None
    __nombre = None
    __carrera = None
    __añoQueCursa = None
    def __init__(self, dni, apellido, nombre, carrera, aqc):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__añoQueCursa = aqc
    def getDni (self):
        return self.__dni
    def getApellido (self):
        return self.__apellido
    def getNombre (self):
        return self.__nombre
    def getAñoQueCursa (self):
        return self.__añoQueCursa
    def __lt__ (self, otroAlum):
        bul = False
        if self.__añoQueCursa < otroAlum.__añoQueCursa:
            bul = True
        return bul
    def mostrar (self):
        print (self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__añoQueCursa)

class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    __alumno = None
    def __init__ (self, dimension, incremento=5):
        self.__alumno = np.empty (dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarAlumno (self, alumno):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumno.resize (self.__dimension)
        self.__alumno[self.__cantidad] = alumno
        self.__cantidad += 1
    def buscarDni (self, dni):
        i=0
        while i<len (self.__alumno) and self.__alumno[i].getDni()!=dni:
            i+=1
        if i<len (self.__alumno):
            bul = True
        else:
            bul = False
        return bul
    def estudiantesAprobados (self, materia, lista):
        i = 0
        bul = False
        print ('DNI / Apellido y Nombre / Fecha / Nota / Año que cursa')
        for mate in lista.getLista ():
            for elem in mate:
                if elem[1]==materia and elem[3]>='7' and elem[4]=='P\n':
                    while self.__alumno[i].getDni() != elem[0]:
                        i+=1
                    print (elem[0], '/', self.__alumno[i].getApellido(), self.__alumno[i].getNombre(), '/', elem[2], '/', elem[3], '/', self.__alumno[i].getAñoQueCursa())
                    bul = True
        return bul
    def ordenar (self):
        self.__alumno.sort ()
    def mostrar (self):
        j=0
        for i in self.__alumno:
            if j<len (self.__alumno):
                i.mostrar()

class ManejadorMaterias:
    __listaMaterias = []
    def __init__ (self, materia):
        self.__listaMaterias.append (materia)
    def getPromedio (self, dni):
        cont = 0
        sum = 0
        for materia in self.__listaMaterias:
            for elem in materia:
                if elem[0] == dni:
                    cont+=1
                    sum += int (elem[3])
        prom = sum/cont
        return prom
    def getLista (self):
        return self.__listaMaterias