from abc import ABC, abstractmethod
import sys

membresias = {
    1: "basica",
    2: "familiar",
    3: "sin Conexión",
    4: "pro"
}

class Membresia(ABC): #Clase Abastracta
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None:
        self.__correo_suscriptor = correo_suscriptor
        self.__nro_tarjeta = nro_tarjeta
        
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor #Para poder obtener este valor desde cualquier parte del programa cuando se llame.
    
    @property
    def nro_tarjeta(self):
        return self.__nro_tarjeta   #Para poder obtener este calor desde cualquier parte del programa cuando se llame. 
    
    @abstractmethod
    def cambiar_suscripcion(self):
        pass
    
    
    def _crea_nva_membrecia(self, nva_membresia):  #Este método es "protected", y se identifica poniendo un _ antes de su nombre.
        if nva_membresia == 1:
            print("Bienvenido a su suscripción: **BASICA**")
            return Basica(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 2:
            print("Bienvenido a su suscripción: **FAMILIAR**")
            return Basica(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 3:
            print("Bienvenido a su suscripción: **SIN CONEXIÓN**")
            return Basica(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        elif nva_membresia == 4:
            print("Bienvenido a su suscripción: **PRO**")
            return Basica(self.correo_suscriptor, self.nro_tarjeta) #Acá estamos haciendo agregación
        else:
            print('Bienvenido a la suscripción: **GRATUITA**')
            sys.exit(1) #Este comando termina la ejecución del programa, se debe importar sys
            
            
class Gratis(Membresia): #Esta es la clase solita del diagrama
    costo = 0
    dispositivos = 1
    def ___init__(self, correo_suscriptor, nro_tarjeta) -> None:
        super().__init__(correo_suscriptor, nro_tarjeta)
        if isinstance(self, Familiar) or isinstance(self, Sin_Conexion): #Acá estamos preguntando si el objeto o instancia pertenece a la clase "Familia" o "Sin_Conexion"
            self.__dias_gratis = 7 #Para hacer una variable protected se deben utilizar __ (2)
        elif isinstance(self, Pro):
            self.__dias_gratis = 15
    
    def cambiar_suscripcion(self, nva_membresia):
        if nva_membresia in [1,2,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self
        
class Basica(Membresia): #Es la que está al lado de la solita y hereda de Membresia
    costo = 3000
    dispositivos = 2
    
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None: #Trae los datos de la Clase Abstracta o Base (Membresia)
        super().__init__(correo_suscriptor, nro_tarjeta)
        if isinstance(self, Familiar) or isinstance(self, Sin_Conexion): #Acá estamos preguntando si el objeto o instancia pertenece a la clase "Familia" o "Sin_Conexion"
            self.__dias_gratis = 7 #Para hacer una variable protected se deben utilizar __ (2)
        elif isinstance(self, Pro):
            self.__dias_gratis = 15
            
    def cancelar_suscripcion(self): #Cuando se llama a cancelar_suscripcion en esa clase, la bajará a "Gratis". Esto es "Agregación"
        return Gratis(self.correo_suscriptor, self.nro_tarjeta)
    
    def cambiar_suscripcion(self, nva_membresia):
        if nva_membresia in [2,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self
        
class Familiar(Basica): #Esta hereda desde la clase anterior que 
    costo = 5000
    dispositivos = 5
    
    def cancelar_suscripcion(self): #Cuando se llama a cancelar_suscripcion en esa clase, la bajará a "Gratis". Esto es "Agregación"
        return Gratis(self.correo_suscriptor, self.nro_tarjeta)
    
    
    def cambiar_suscripcion(self, nva_membresia):
        if nva_membresia in [1,3,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self
        
    def control_parental(self):
        pass
    
class Sin_Conexion(Basica): #Esta hereda desde la clase anterior
    costo = 3500
    dispositivos = 2

    def cambiar_suscripcion(self, nva_membresia): #Acá estamos cambiando de membresia (las existentes) ACá estamos hablando del polimorfismo. Sobreescritura del metodo en cada clase
        if nva_membresia in [1,2,4]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self
    
    def contenido_max(self):
        pass
    
class Pro(Familiar, Sin_Conexion):
    costo = 7000
    dispositivos = 6
        
    def cambiar_suscripcion(self, nva_membresia): #Acá estamos cambiando de membresia (las existentes)
        if nva_membresia in [1,2,3]:
            return self._crea_nva_membrecia(nva_membresia)
        else:
            return self




g = Gratis("correo@correo.cl",5470123456781234)

print(type(g))
print("Costo de la suscripción: ", g.costo)
print("Dispositivos permitidos: ", g.dispositivos)

b = g.cambiar_suscripcion(1)
print("Costo de la suscripción: ", b.costo)
print("Dispositivos permitidos: ", b.dispositivos)

f = b.cambiar_suscripcion(2)
print("Costo de la suscripción: ", f.costo)
print("Dispositivos permitidos: ", f.dispositivos)

f = f.cambiar_suscripcion(1)
print("Costo de la suscripción: ", f.costo)
print("Dispositivos permitidos: ", f.dispositivos)
    
f = f.cambiar_suscripcion(4)
print("Costo de la suscripción: ", f.costo)
print("Dispositivos permitidos: ", f.dispositivos)

# cancelar la suscripción del usuario "f" en este momento es "Pro", por consecuencia, nos debería dejar en "Gratis"

f = f.cancelar_suscripcion()
print("Costo de la suscripción: ", f.costo)
print("Dispositivos permitidos: ", f.dispositivos)
    
    
            
