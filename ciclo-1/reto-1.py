# RETO 1
# David Monroy

def main() -> None:
    print(cdt('AB1012', 1_000_000, 3))
    print(cdt('ER3366', 650_000, 2))
    print(cdt('QW3456', 5_000_000, 2))

def cdt(usuario: str, capital: int, tiempo: int) -> str:
    PORCENTAJE_INTERES = 0.03
    PORCENTAJE_INTERES_A_PERDER = 0.02

    if tiempo <= 2:
        valor_a_perder: float = capital * PORCENTAJE_INTERES_A_PERDER
        valor_total = round(capital - valor_a_perder, 1)

        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"


    valor_intereses: float = (capital * PORCENTAJE_INTERES * tiempo) / 12
    valor_total = valor_intereses + capital

    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"

if __name__ == '__main__':
    main()