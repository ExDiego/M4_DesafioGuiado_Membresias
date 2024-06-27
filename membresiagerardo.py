from abc import ABC, abstractmethod
import sys

membresias = {
    1: "basica",
    2: "familiar",
    3: "sin Conexion",
    4: "pro"
}

class Membresia(ABC): #Clase Abstracta
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None:
        self.__correo_suscriptor = correo_suscriptor
        self.__nro_tarjeta = nro_tarjeta
    
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor #Para poder obtener este valor desde cualquier parte del programa cuando se llame.
    
    @property
    def nro_tarjeta(self):
        return self.__nro_tarjeta #Para obtener este valor desde cualquier parte del programa cuando se llame.
    
    @abstractmethod
    def cambiar_suscripcion(self):
        pass

    def _crea_nva_membrecia(self, nva_membresia): #Este método es "protected", y se indentifica poniendo un _ antes de su nombre.
        if nva_membresia == 1:
            print("Bienvenido a su suscripción: **BASICA**")
            return Basica(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 2:
            print("Bienvenido a su suscripción: **FAMILIAR**")
            return Familiar(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 3:
            print("Bienvenido a su suscripción: **SIN CONEXIÓN**")
            return Sin_Conexion(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 4:
            print("Bienvenido a su suscripción: **PRO**")
            return Pro(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        else:
            print('No se reconoce membresía.')
            sys.exit(1) #Este comando termina la ejecución del programa... 

class Gratis(Membresia): #Esta es la clase solita del diagrama
    costo = 0
    dispositivos = 1
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None:
        super().__init__(correo_suscriptor, nro_tarjeta)
        print("... Su suscripción es GRATUITA... :/ ")
            
    def cambiar_suscripcion(self, nva_membresia): #Desde Gratis se puede cambiar a basica, familiar, sin conexion o Pro (1, 2, 3 o 4)
        if nva_membresia in [1,2,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self

class Basica(Membresia): #es la que está al lado de la solita y hereda de Membresia
    costo = 3000
    dispositivos = 2
    
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None:  #Trae los datos de la Clase Abstracta o Base (Membresia)
        super().__init__(correo_suscriptor, nro_tarjeta)
        if isinstance(self, Familiar) or isinstance(self, Sin_Conexion): #Acá estamos preguntando si el objeto o instancia pertenece a la clase "Familiar" o "Sin_Conexion"
            self.__dias_gratis = 7 #Para hacer una variable protected se deben utilizar __ (2)
        elif isinstance(self, Pro):
            self.__dias_gratis = 15
        
    def cancelar_suscripcion(self): #Cuando se llame a Cancelar_suscripcion en esta Clase, la bajará a "Gratis".  Esto es "Agregación"
        return Gratis(self.correo_suscriptor, self.nro_tarjeta )

    def cambiar_suscripcion(self, nva_membresia): #Acá estamos en la Memembresia Basica, por lo que el cambio deberá realizarse desde 2 a 4 que son membresia mayores.
        if nva_membresia in [2,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self

class Familiar(Basica): #Esta hereda desde la clase anterior que hereda de la Abstranda "Membresia"
    costo = 5000
    dispositivos = 5

    def cambiar_suscripcion(self, nva_membresia): #Acá estamos cambiando de membresia (las existentes)
        if nva_membresia in [1,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self
    
    def contro_parental(self):
        pass

class Sin_Conexion(Basica): #Esta hereda desde la clase anterior que hereda de la Abstranda "Membresia"
    costo = 3500
    dispositivos = 2

    def cambiar_suscripcion(self, nva_membresia): #Acá estamos cambiando de membresia (las existentes) ACÁ ESTAMOS HALBANDO DEL POLIFORMISMO - SOBREESCRITURA DE MÉTODO EN CADA CLASE
        if nva_membresia in [1,2,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self

    def contenido_max(self):
        pass

class Pro(Familiar,Sin_Conexion):
    costo = 7000
    dispositivos = 6
    
    def cambiar_suscripcion(self, nva_membresia): #Acá estamos cambiando de membresia (las existentes)
        if nva_membresia in [1,2,3]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self


# def main():
#     pass

# if __name__ == '__main__':
#     main()

# pruebas

g = Gratis("correo@correo.cl", 5470123456781234)

print(type(g))
print("Costo de la suscripcion: ", g.costo)
print("Dispositivos permitidos:", g.dispositivos)

b = g.cambiar_suscripcion(1)
print("Costo de la suscripcion: ", b.costo)
print("Dispositivos permitidos:", b.dispositivos)

f = b.cambiar_suscripcion(2)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

f = f.cambiar_suscripcion(1)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

f = f.cambiar_suscripcion(4)
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

#Vamos a cancelar la suscripción del usuario "f" en en este momento es "Pro", Por consecuencia, nos debería dejar en el gratis

f = f.cancelar_suscripcion()
print("Costo de la suscripcion: ", f.costo)
print("Dispositivos permitidos:", f.dispositivos)

#Vamos a dar una número de membremsia que no existe...

f = f.cambiar_suscripcion(5)