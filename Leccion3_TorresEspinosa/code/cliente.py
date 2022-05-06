from producto import *
#Variable para funcionar con cliente, Leer BBDD
if __name__ == "__main__":
    disp = [Producto("stout", 4.5, 3), Producto("ipa", 3.75, 5), Producto("ale", 2.75, 8), Producto("pastry", 5, 4)]

#CLASE DIRECCION, el cliente prodrá guardar mas de una direccion
class Direccion:
    """Clase que instancia una Dirección.
    """
    #___INIT___
    def __init__(self, calle, numero, lugar, cp, provincia, pais):
        """Constructor de Dirección.

        :param calle: Nombre de la calle
        :type calle: :class: `str`
        :param numero: Número de la dirección
        :type numero: :class: `int`
        :param lugar: Población
        :type lugar: :class: `str`
        :param cp: Código Postal
        :type cp: :class: `int`
        :param provincia: Provincia
        :type provincia: :class: `str`
        :param pais: País
        :type pais: :class: `str`
        """
        self.__calle = calle
        self.__numero = numero
        self.__lugar = lugar
        self.__cp = cp
        self.__provincia = provincia
        self.__pais = pais

    #Get
    def get_direccion(self):
        """Método para obtener los atributos de la dirección.

        :return: calle, número, población, cp, país
        :rtype: :class: `str`, `int`
        """
        return self.__calle, self.__numero, self.__lugar, self.__provincia, self.__cp, self.__pais

#CLASE CLIENTE
class Cliente:
    """Clase que instancia un cliente.

    :param numero: Cantidad de clientes creados.
    :type numero: :class: `int`
    """
    numero = 0
    #__INIT__
    def __init__(self, nombre, mail = "", tlfn = 123456789):
        """Constructor del cliente.

        :param nombre: Nombre del cliente.
        :type nombre: :class: `str`
        :param mail: correo electrónico, defaults to ""
        :type mail: :class: `str`, optional
        :param tlfn: Teléfono de contacto, defaults to 123456789
        :type tlfn: :class: `int`, optional
        :param direccion: lista de direcciones del cliente.
        :type direccion: :class: list(`Direccion`) 
        :param cesta: lista de productos para la compra del cliente.
        :type cesta: :class: list(`producto.Producto`) 
        """
        self.__nombre = nombre
        self.__mail = mail
        self.__tlfn = tlfn
        self.__direccion = []
        self.__cesta = [] #Dict or tuple?
        Cliente.numero += 1
        print(f"-> Cliente Nuevo. Nº: {Cliente.numero}")

    #Getters
    def get_cliente(self):
        """Método para ver los datos del cliente. Nombre, teléfono y mail.
        """
        print(f"{self.__nombre} {self.__tlfn}\n{self.__mail}\n")

    def get_nombre(self):
        """Método para obtener el nombre del cliente.

        :return: Nombre del cliente
        :rtype: :class: `str`
        """
        return self.__nombre

    def get_direccion(self):
        """Método para visualizar los datos de la dirección del cliente.
        """
        '''l = self.direccion.copy()
        print(f"\n\t Direccion de {self.get_nombre()}:")
        for i in l:
            i.get_direccion()'''
        print(f"\n\t Direccion de {self.get_nombre()}:")
        for i in self.__direccion:
            calle, numero, lugar, prov, cp , pais = i.get_direccion()
            print(f"C/ {calle} Nº: {numero}")
            print(f"{lugar}({prov}) {cp}")
            print(f"{pais}")
            print('\n')

    def get_cesta(self):
        """Método para obtener la cesta de compra del cliente.

        :return: Copia de la cesta de la compra
        :rtype: :class: list(`producto.Producto`)
        """
        return self.__cesta.copy()
            
    #Setters
    if __name__ == "__main__":
        def add_producto(self, name, amount):
            """Método para manejar la introducción de stock de los productos

            :param name: nombre del producto.
            :type name: :class: `str`
            :param amount: cantidad de artículos de dicho producto.
            :type amount: :class: `int`
            """
            i = 0
            while (name != disp[i].get_nombre()): #Podria cambiar a punteros o por index()
                i += 1
            p = Producto(disp[i].get_nombre(), disp[i].get_precio(), amount) #Arreglar lo del precio debido a que seria privado para el cliente pero solo podria verlo
            self.__cesta.append(p)
            print(f"\t-> Añadido {amount} {disp[i].get_nombre()}")
            disp[i].set_stock(disp[i].get_stock() - amount)

            if disp[i].get_stock() == 0:
                            print(f"\t-> Se acabo el stock de {disp[i].get_nombre()}")
    else:
        def add_producto(self, p):
            """Método para añadir productos a la cesta del cliente

            :param p: producto que se va añadir
            :type p: :class: `producto.Producto`
            """
            #__shop.py__
            if existe(p.get_nombre(), self.__cesta):
                i = buscar_id(p.get_nombre(), self.__cesta)
                self.__cesta[i].set_stock(self.__cesta[i].get_stock() + p.get_stock())
            else:
                self.__cesta.append(p)

            print(f"\t-> Añadido {p.get_stock()} {p.get_nombre()}")

    def add_direccion(self):
        """Método para añadir una dirección al cliente.
        """
        print("\tIntroduciendo los datos de la direccion del cliente:")
        calle = input("\tCalle: ")
        numero = input("\tNumero: ")
        lugar = input("\tPoblacion: ")
        cp = input("\tC.P.:")
        provincia = input("\tProvincia: ")
        pais = input("\tPais: ")

        self.__direccion.append(Direccion(calle, numero, lugar, cp, provincia, pais))

if __name__ == "__main__":

    c = Cliente("Chinook", "asdfg@asf.com", 687550062)

    c.get_cliente()

    print("*****")

    c.get_cesta()

    c.add_direccion()

    c.get_direccion()