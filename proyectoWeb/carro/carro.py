class Carro():
    def __init__(self, request):
        self.request = request
        self.session = request.session     #con respecto al inicio de secion del usuario
        carro = self.session.get("carro")  #tomamos el diccionario carro de la secion del usario
        if not carro:
            carro = self.session["carro"] = {}   #Inicializamos el carro de la session en vacio
        self.carro = carro    #creando un carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        self.guardarCarro()
    
    def guardarCarro(self):    #Guarda todos los elementos del carro dependiendode la session
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardarCarro()

    def restarProducto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardarCarro()
    
    def limpiarCarro(self):
        carro = self.session["carro"] = {}
        self.session.modified = True