from Nodo import Nodo

class Lista():
    

    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def Vacia(self):
        return self.primero == None
    
    def Agregar(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = dato
        else: 
            aux = self.ultimo
            self.ultimo = dato
            dato.atras = aux
            aux.siguiente = dato

    def Buscar(self,identificador):
        aux = self.primero
        if self.primero == self.ultimo:
            if identificador == aux.identificador:
                return aux
        else:
            while aux != None:
                if (identificador) == (aux.identificador):
                    return aux
                aux = aux.siguiente

    def BuscarMatriz(self,nombre):
        aux = self.primero
        if self.primero == self.ultimo:
            if nombre== aux.nombre:
                return aux
        else:
            while aux != None:
                if nombre == aux.nombre:
                    return aux
                aux = aux.siguiente
    
    def Imprimir(self):
        aux = self.primero
        while(aux != None):
            print(aux.dato)
            aux = aux.siguiente

    def Print(self):
        aux = self.primero
        x = 1
        while(aux != None):
            print(x)
            print(aux.dato.fecha)
            print(aux.dato.reportado)
            aux.dato.afectado.Imprimir()
            print(aux.dato.error)
            aux = aux.siguiente
            x = x + 1


    def ExisteNodo(self,identificador, tipo):
        aux = self.primero
        if aux == None :
            return False
        else:  
            if self.primero == self.ultimo:
                if identificador == aux.identificador:
                    return True
            else:
                while aux != None:
                    if identificador == aux.identificador:
                        return True
                    aux = aux.siguiente
            return False

    def get_Primero(self):
        return self.primero

   

    
    