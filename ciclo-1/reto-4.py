# Reto 4
# David Monroy


def main() -> None:
    ordenes([[1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
            [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
            [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
            [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]])

    ordenes([[6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
            [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
            [6591, ("7812", 2, 11.99), ("9652",11,18.99)]])


def ordenes(rutina_contable: list) -> None:
    print("{:-^50}".format(" Inicio Registro Diario "))
    for item in rutina_contable:

        num_factura: int = item[0]
        total: float = 0

        for sub_item in item[1:]:
            # Getting the price
            precio: float = sub_item[-1]

            # Getting the quantity
            cantidad: int = sub_item[-2]

            total += precio * cantidad
        
        if precio < 600_000:
            total += 25_000

        print(f"La factura {num_factura} tiene un total en pesos de {round(total, 2)}")

    print("{:-^50}".format(" Fin Registro Diario "))


if __name__ == '__main__':
    main()