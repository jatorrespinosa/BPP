def existe(name, lista):
    """Función que comprueba si existe un nombre en la lista.

    :param name: nombre del objeto de la consulta.
    :type name: :class: `str`
    :param lista: lista de productos para consultar.
    :type lista: :class: `Producto`
    :return: retorna True si encuentra lo buscado.
    :rtype: :class: `boolean`
    """
    check = False
    #Recorre datos
    for i in lista:
        #si hay coincidencia existe
        if name == i.get_nombre():
            check = True
            break
    return check

def buscar_id(name, lista):
    """Función que busca el id de un nombre en una lista dada.
    Comprueba si existe antes el producto.

    :param name: nombre del objeto de la consulta.
    :type name: :class: `str`
    :param lista: lista de productos para consultar.
    :type lista: :class: `Producto`
    :return: retorna id si existe lo buscado.
    :rtype: :class: `int`
    """
    if existe(name, lista):
        i = 0
        while (name != lista[i].get_nombre()):
                i += 1
        return i

#CLASE OPINIONES, el producto albergara una lista de opiniones
class Opiniones:
    """Clase para opiniones personales.
    """
    #__INIT__
    def __init__(self, nombre, valor, text):
        """Constructor de opinión.

        :param nombre: Nombre del autor de la opinión.
        :type nombre: :class: `str`
        :param valor: valoración del producto.
        :type valor: :class: `int`
        :param text: descripción de la opinión.
        :type text: :class: `str`
        """
        self.__nombre = nombre
        self.__valor = valor
        self.__text = text
    
    #Getters
    def get_nombre(self):
        """Método para obtener el nombre de una opinión.

        :return: nombre
        :rtype: :class: `str`
        """
        return self.__nombre

    def get_valor(self):
        """Método para obtener la valoración de una opinión.

        :return: valor
        :rtype: :class: `int`
        """
        return self.__valor

    def get_text(self):
        """Método para obtener la descripción de una opinión.

        :return: descripción (text)
        :rtype: :class: `str`
        """
        return self.__text

#CLASE PRODUCTO
class Producto:
    """Clase que instancia un producto.

    :param cantidad: Cantidad de productos creados.
    :type cantidad: :class: `int`
    """
    #Numero de productos creados
    cantidad = 0

    #__INIT__
    def __init__(self, nombre, precio = 0.0, stock = 0):
        """Constructor de producto. Aumenta en uno la cantidad total de productos.

        :param nombre: nombre del producto
        :type nombre: :class: `str`
        :param precio: valor del producto, defaults to 0.0
        :type precio: :class: `float`, optional
        :param stock: cantidad de stock de dicho producto, defaults to 0
        :type stock: :class: `int`, optional
        :param op_list: lista de opiniones del producto
        :type op_list: :class: list(`Opiniones`) 
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__op_list = []
        Producto.cantidad += 1

    #Getters
    def get_producto(self):
        """Método para obtener el nombre, el precio y el stock del producto.

        :return: nombre, precio y stock.
        :rtype: :class: `str`, `float`, `int`
        """
        return self.__nombre , self.__precio , self.__stock

    def get_nombre(self):
        """Método para obtener el nombre del producto.

        :return: nombre
        :rtype: :class: `str`
        """
        return self.__nombre

    def get_stock(self):
        """Método para obtener el stock del producto.

        :return: stock
        :rtype: :class: `int`
        """
        return self.__stock

    def get_precio(self):
        """Método para obtener el precio del producto.

        :return: precio
        :rtype: :class: `float`
        """
        return self.__precio

    def get_opinion(self):
        """Método para obtener las opiniones del producto.

        :return: lista de opiniones
        :rtype: :class: `Opiniones`
        """
        for i in self.__op_list:
            print(f"{i.get_nombre()} {i.get_valor()}/10\n{i.get_text()}\n")
    
    #Setters        
    def set_producto(self, nombre, precio = 0.0, stock = 0):
        """Método para modificar el nombre, el precio y el stock del producto.
        Si no hay precio o stock no los varia.
        """
        self.__nombre = nombre
        #Si no hay precio o stock no los varia
        if precio != 0.0:
            self.__precio = precio
        if stock != 0:
            self.__stock = stock

    def set_stock(self, stock):
        """Método para modificar el stock del producto.
        """
        self.__stock = stock

    def set_precio(self, precio):
        """Método para modificar el precio del producto.
        """
        self.__precio = precio
        
    def add_opinion(self, nombre, valor, text):
        """Método para añadir una opinión a la lista del producto.
        """
        op = Opiniones(nombre, valor, text)
        self.__op_list.append(op)
    
    

if __name__ == "__main__":
    #Prueba funcionan getters and setters producto
    b = Producto("stout", 5, 10)

    b.get_producto()
    print('\n')

    b.set_precio(5.5)


    b.set_stock(5)


    b.get_producto()
    print('\n')

    b.set_producto("ale")


    b.get_producto()
    print('\n')

    b.get_precio()
    print('\n')

    b.get_stock()
    print('\n')

    #Prueba funcionan opiniones
    b = Producto("stout", 5, 10)
    b.add_opinion("Jesus", 8.7, "Me ha encantado.")
    b.add_opinion("Manuel", 6.3, "No es lo que esperaba, pero funciona.")
    b.get_opinion()