class Persona():

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def compara_edad(self, otro):
        if self.edad() > otro.edad():
            print(f"{otro.nombre()} es más joven que yo.")
        elif self.edad() < otro.edad():
            print(f"{otro.nombre()} es más viejo que yo.")
        else:
            print(f"{otro.nombre()} tiene la misma edad que yo.")
