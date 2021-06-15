from abc import abstractmethod



class Categoria:

    @classmethod    
    def crear_y_asignar_categoria(cls, cliente, compras_filtradas):
        for c in cls.__subclasses__():
            if c.evaluar(compras_filtradas):
                nueva_categoria = c()
                cliente.asignar_categoria(nueva_categoria)

    @classmethod
    def evaluar(compras:list) -> bool:
        return False

class ClienteVIP(Categoria):
    
    @classmethod
    def evaluar(compras:list) -> bool:
        monto = 0
        for c in compras:
            monto += c.monto
        return monto > 5000

class ClienteNormal(Categoria):
    
    @classmethod
    def evaluar(compras:list) -> bool:
        monto = 0 
        for c in compras:
            monto += c.monto
        return monto <= 0

