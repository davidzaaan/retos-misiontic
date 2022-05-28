# Reto 3
# David Monroy


def main() -> None:
    print(consultar_registro(auto_partes([(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010))

    print(consultar_registro(auto_partes([(5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001))

    print(consultar_registro(auto_partes([(9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852))


def auto_partes(ventas: list) -> list:
    """
    Function that returns a list of dictionaries with the data of the car parts and its owners
    params:
       ventas[list]: This is the records list to store values
    returns:
       registro[list]: The new list with the respective data dictionary of each owner 
    """
    caracteristicas: list = ['IdProducto', 'dProducto', 'pnProducto',
    'cvProducto', 'sProducto', 'nComprador', 'cComprador', 'fVenta']
    
    registro: list = []

    for elem in ventas:
        datos: dict = dict(zip(caracteristicas, elem)) # getting the data
        registro.append(datos)

    return registro
    

def consultar_registro(ventas: list, id_producto: int) -> str:
    """
    Function that returns whether a record exists within the passed list
    params:
       ventas[list]: This is the records list to store values
       id_producto[int]: Id of the product to lookup
    returns:
       salida[str]: The human-readable information with the customer information if found
    """
    registro_encontrado = None

    for item in ventas:
        if item['IdProducto'] == id_producto:
            registro_encontrado = item
            
    if registro_encontrado:
        salida: str = f"Producto consultado : {registro_encontrado['IdProducto']} "\
        +f"Descripción {registro_encontrado['dProducto']} "\
        +f"#Parte {registro_encontrado['pnProducto']} "\
        +f"Cantidad vendida {registro_encontrado['cvProducto']} "\
        +f"Stock {registro_encontrado['sProducto']} "\
        +f"Comprador {registro_encontrado['nComprador']} "\
        +f"Documento {registro_encontrado['cComprador']} "\
        +f"Fecha Venta {registro_encontrado['fVenta']}"
    else:
        salida: str = 'No hay registro de venta de ese producto'

    return salida


if __name__ == '__main__':
    main()