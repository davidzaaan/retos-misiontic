# Reto 2
# David Monroy

CLIENTES: list = []

def main() -> None:
    print(cliente({'nombre': 'Gloria Suarez', 'edad': 3, 'primer_ingreso': True}))
    print(cliente({'nombre': 'Johana Fernandez', 'edad': 20, 'primer_ingreso': True}))
    print(cliente({'nombre': 'Johana Fernandez', 'edad': 20, 'primer_ingreso': False}))
    print(cliente({'nombre': 'Tatiana Suarez', 'edad': 17, 'primer_ingreso': True}))
    print(cliente({'nombre': 'Tatiana Suarez', 'edad': 17, 'primer_ingreso': False}))
    print(cliente({'nombre': 'Tatiana Ruiz', 'edad': 8, 'primer_ingreso': True}))
    print(cliente({'nombre': 'Tatiana Ruiz', 'edad': 8, 'primer_ingreso': False}))


def cliente(informacion: dict) -> dict:
    salida: dict = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atraccion(informacion['edad']),
        'apto': (informacion['edad'] >= 7),
        'primer_ingreso': informacion['primer_ingreso']
    } 

    if not informacion['nombre'] in CLIENTES:
        salida['primer_ingreso'] = True
        salida['total_boleta'] = valor_con_descto(informacion['edad'])
        CLIENTES.append(informacion['nombre'])
    else:
        salida['primer_ingreso'] = False
        salida['total_boleta'] = valor(informacion['edad'])

    return salida


def atraccion(edad: int) -> str:
    if edad < 7: return "N/A"

    if edad > 18:
        atraccion: str = "X-Treme"
    elif edad >= 15:
        atraccion: str = "Carroschocones"
    elif edad >= 7:
        atraccion: str = "Sillas voladoras"

    return atraccion


def valor(edad: int) -> int:
    if edad < 7: return "N/A"

    if edad > 18:
        valor_total: float = 20_000
    elif edad >= 15:
        valor_total: float = 5_000
    elif edad >= 7:
        valor_total: float = 10_000

    return valor_total


def valor_con_descto(edad: int) -> float or str:
    try:
        valor_boleta: int = int(valor(edad))
    except ValueError:
        return "N/A"

    if edad > 18:
        descuento: float = valor_boleta * 0.05
    elif edad >= 15:
        descuento: float = valor_boleta * 0.07
    elif edad >= 7:
        descuento: float = valor_boleta * 0.05

    valor_total_boleta: float = valor_boleta - descuento

    return valor_total_boleta
        


if __name__ == '__main__':
    main()