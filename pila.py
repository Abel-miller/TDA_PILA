class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.append(item)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("Eliminar de una pila vacía")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("Ver el tope de una pila vacía")

    def tamano(self):
        return len(self.items)


def evaluar_expresion(expresion):
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    pila = Pila()

    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            pila.insertar(int(token))
        elif token in operadores:
            operando2 = pila.eliminar()
            operando1 = pila.eliminar()
            resultado = operadores[token](operando1, operando2)
            pila.insertar(resultado)
        else:
            raise ValueError("Token inválido: {}".format(token))

    return pila.eliminar()


def main():
    expresion = input("Ingrese una expresión en notación polaca inversa: ")
    try:
        resultado = evaluar_expresion(expresion)
        print("Resultado de la expresión:", resultado)
    except (ValueError, IndexError) as error:
        print("Error al evaluar la expresión:", error)


if __name__ == "__main__":
    main()
